from django.views.generic import TemplateView

from apps.first_example.services.generate_humans import generate_humans


class HumansView(TemplateView):
    template_name = "first_example/humans.html"

    def get_context_data(self, amount: int = 7, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)

        context_data["title"] = "Humans"

        context_data["humans"] = generate_humans(amount=amount)

        return context_data
