from django.apps import AppConfig


class AnimalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.animals"

    def ready(self):
        from . import signals  # noqa: F401
