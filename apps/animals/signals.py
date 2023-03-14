from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def change_owner(sender, instance: User, **kwargs):
    if owner := instance.owner:
        if (user_full_name := instance.get_full_name()) != owner.name:
            owner.name = user_full_name
            owner.save()
