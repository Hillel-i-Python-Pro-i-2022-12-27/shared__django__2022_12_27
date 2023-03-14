from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("update_user/<int:pk>/", login_required(views.UserUpdateView.as_view()), name="update_u"),
    path("logout", views.logout_request, name="logout"),
]
