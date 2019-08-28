from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class QuizTaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        QuizTaker.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.quiztaker.save()