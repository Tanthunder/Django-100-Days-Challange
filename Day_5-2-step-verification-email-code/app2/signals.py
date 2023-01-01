from app1.models import CustomUser
from .models import Code

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def post_save_code_generate(sender, instance, created, *args, **kwargs):
    """Utilizing post_save signal to generate code."""
    if created:
        Code.objects.create(user=instance)