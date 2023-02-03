from django.urls import path

from . import views

# from apps.first_example.views.index import index

app_name = "root"

urlpatterns = [
    # path("", index, name="index"),
    path("", views.index, name="index"),
]
