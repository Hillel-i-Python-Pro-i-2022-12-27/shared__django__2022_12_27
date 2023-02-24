from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

app_name = "animals"

urlpatterns = [
    path(
        "list/",
        include(
            [
                path("by-function/", views.list_animals, name="list_by_function"),
                path("by-class/", views.AnimalListView.as_view(), name="list_by_class"),
            ]
        ),
    ),
    path("create/", login_required(views.AnimalCreateView.as_view()), name="create"),
    path("update/<int:pk>/", views.AnimalUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.AnimalDeleteView.as_view(), name="delete"),
]
