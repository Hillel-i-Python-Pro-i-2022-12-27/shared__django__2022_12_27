from django.urls import path, include

from . import views

app_name = "first_example"

urlpatterns = [
    path(
        "hello/",
        include(
            [
                # path("", views.greetings, name="index"),
                # path("<str:name>/<int:age>", views.greetings, name="hello_with_args"),
                path("", views.GreetingsView.as_view(), name="index"),
                path("<str:name>/<int:age>/", views.GreetingsView.as_view(), name="hello_with_args"),
            ]
        ),
    ),
    path("humans/", views.HumansView.as_view(), name="humans"),
]
