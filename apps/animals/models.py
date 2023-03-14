from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Kind(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Owner(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name="owner",
        default=None,
        null=True,
        blank=True,
    )

    session_key = models.CharField(
        max_length=100,
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(
        blank=True,
        default=0,
    )

    owner = models.ForeignKey(
        Owner,
        on_delete=models.SET_NULL,
        related_name="animals",
        default=None,
        null=True,
        blank=True,
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
        null=False,
        blank=False,
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
