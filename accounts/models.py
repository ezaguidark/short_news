from django.db import models
# En este caso practico se importa el modelo AbstractUser para crear nuestro modelo de Usuario
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=500)