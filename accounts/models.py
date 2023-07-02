# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=lambda instance, filename: f"profile_images/{instance.user.username}.png", blank=True)

    def __str__(self):
        return self.user.username

