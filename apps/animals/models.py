from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(
        blank=True,
        default=0,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    avatar = models.ImageField(
        max_length=255,
        upload_to="animals/animal/avatar/",
        blank=True,
        null=True,
    )

    kind = models.ForeignKey(
        Kind,
        on_delete=models.CASCADE,
        related_name="animals",
        default=None,
        null=True,
        blank=True,
    )

    # state = models.CharField(
    #     choices=(
    #         ('alive', 'Alive'),
    #         ('dead', 'Dead'),
    #     ),
    # )

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    __repr__ = __str__
