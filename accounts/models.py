from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(
    post_save, sender=User, dispatch_uid="create_user_token"
)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)




