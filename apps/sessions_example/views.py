from typing import Final

from django.contrib.sessions.backends.cached_db import SessionStore
from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"


# Create your views here.
class SessionExampleView(TemplateView):
    template_name = "sessions_example/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session

        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[KEY__COUNT_OF_VISITS] = count_of_visits

        context = super().get_context_data(**kwargs)
        context["title"] = "Session example"
        context["session_id"] = session.session_key
        context["count_of_visits"] = count_of_visits
        return context
