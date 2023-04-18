import logging
import random
import uuid
from time import sleep

from celery import shared_task


# from apps.celery_example.tasks import example_2


@shared_task
def example_1(value: str):
    logger = logging.getLogger("django")

    id_ = uuid.uuid4()

    logger.info(f"[{id_}] example_1: {value}")
    wait_for = random.randint(1, 10)
    logger.info(f"[{id_}] example_1: wait_for: {wait_for}")
    sleep(wait_for)
    logger.info(f"[{id_}] example_1: completed")

    # example_2.delay()

    return
