import typing

from faker import Faker

from apps.animals import models


def generate_animals(amount: int = 10, is_mark_as_autogenerated: bool = False) -> typing.Iterator[models.Animal]:
    fake = Faker()

    kind, _ = models.Kind.objects.get_or_create(
        name="Animal",
    )

    owner, _ = models.Owner.objects.get_or_create(
        name="Auto generated owner",
    )

    for _ in range(amount):
        yield models.Animal(
            name=fake.first_name(),
            age=fake.random_int(min=0, max=100),
            #
            is_auto_generated=is_mark_as_autogenerated,
            #
            kind=kind,
            owner=owner,
        )
