from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name="index.html",
    )
