from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if kwargs.get("raw", False):
        return

    if created:
        Profile.objects.get_or_create(
            user=instance,
            defaults={
                "username": instance.username,
                "email": instance.email,
            },
        )


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if kwargs.get("raw", False):
        return

    if hasattr(instance, "profile"):
        instance.profile.save()
