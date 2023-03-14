import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView, RedirectView
from faker import Faker

from apps.animals.forms import AnimalByOwnerForm
from apps.animals.models import Animal, Owner, Kind


def list_animals(request):
    return render(
        request=request,
        template_name="animals/animal_list.html",
        context={
            "object_list": Animal.objects.all(),
        },
    )


class AnimalListView(ListView):
    model = Animal
    queryset = Animal.objects.all().order_by("-modified_at")


class AnimalCreateView(CreateView):
    model = Animal
    fields = (
        "name",
        "age",
        "kind",
        "avatar",
        "is_auto_generated",
    )
    success_url = reverse_lazy("animals:list_by_class")


@method_decorator(login_required, name="dispatch")
class AnimalUpdateView(UpdateView):
    model = Animal
    fields = (
        "id",
        "name",
        "age",
        "kind",
        "avatar",
        "is_auto_generated",
    )
    success_url = reverse_lazy("animals:list_by_class")


class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy("animals:list_by_class")


class AnimalsOwnersListView(TemplateView):
    template_name = "animals/animals_owners_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        owners = Owner.objects.all().annotate(count_animals=Count("animals"))

        context["object_list"] = owners
        return context


class GoToMyAnimalsView(RedirectView):
    # permanent = False
    # query_string = True
    # pattern_name = "animals:animals_list_by_owner"

    def get_redirect_url(self, *args, **kwargs):
        session = self.request.session
        session_key = session.session_key

        if session_key is None:
            session.save()
            session_key = session.session_key

        user = self.request.user
        if user.is_authenticated:
            owner, _ = Owner.objects.get_or_create(
                user=user,
                defaults={
                    "name": user.username,
                    "session_key": session_key,
                },
            )
            if owner.session_key != session_key:
                owner.session_key = session_key
                owner.save()
        else:
            name = Faker().name()
            owner, _ = Owner.objects.get_or_create(
                session_key=session_key,
                defaults={
                    "name": name,
                },
            )

        owner_id = owner.id
        return reverse_lazy("animals:animals_list_by_owner", kwargs={"pk": owner_id})


class AnimalsListByOwner(FormView):
    template_name = "animals/animal_list_by_owner.html"
    form_class = AnimalByOwnerForm

    def get_initial(self):
        initial = super().get_initial()
        owner_id = self.kwargs.get("pk")

        initial["owner"] = owner_id

        initial["name"] = Faker().name()
        initial["age"] = random.randint(1, 20)

        # TODO Get random kind. If not exists, create it.
        initial["kind"] = random.choice(Kind.objects.all().values_list("pk", flat=True))

        return initial

    def get_success_url(self):
        return reverse_lazy("animals:animals_list_by_owner", kwargs={"pk": self.kwargs.get("pk")})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owner_id = self.kwargs.get("pk")

        owner = Owner.objects.get(pk=owner_id)

        context["owner"] = owner

        context["object_list"] = owner.animals.all().order_by("-modified_at")
        return context

    def form_valid(self, form):
        if form.instance.owner_id != self.kwargs.get("pk"):
            raise ValidationError("Invalid owner")

        form.save()
        return super().form_valid(form)
