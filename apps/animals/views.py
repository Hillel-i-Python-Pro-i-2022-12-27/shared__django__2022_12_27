from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.animals.models import Animal


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
