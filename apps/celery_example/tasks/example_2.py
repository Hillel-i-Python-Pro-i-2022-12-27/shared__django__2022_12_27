import logging
import random
import uuid
from time import sleep

from celery import shared_task


@shared_task
def example_2():
    logger = logging.getLogger("django")

    id_ = uuid.uuid4()

    logger.info(f"[{id_}] example_2")
    wait_for = random.randint(1, 10)
    logger.info(f"[{id_}] example_2: wait_for: {wait_for}")
    sleep(wait_for)
    logger.info(f"[{id_}] example_2: completed")

    return
