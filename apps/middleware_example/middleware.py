import logging
from typing import ClassVar
from collections.abc import Callable


class SimpleMiddleware:
    _NAME: ClassVar[str] = "first"

    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request):
        self.logger.info(f"Before {self._NAME}")
        response = self.get_response(request)
        self.logger.info(f"After {self._NAME}")
        return response


class SimpleMiddleware2(SimpleMiddleware):
    _NAME: ClassVar[str] = "second"
