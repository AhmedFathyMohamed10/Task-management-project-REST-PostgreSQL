from django.db import models
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


class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(
    post_save, sender=User, dispatch_uid="create_user_profile"
)
def update_user_first_last_name(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )

