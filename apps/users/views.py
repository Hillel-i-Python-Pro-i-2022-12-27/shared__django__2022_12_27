from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from apps.users.forms import RegisterUserForm

User = get_user_model()


class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("root:index")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"


class UserUpdateView(UpdateView):
    model = User

    template_name = "registration/edit.html"
    fields = (
        "username",
        "email",
    )
    success_url = reverse_lazy("root:index")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
