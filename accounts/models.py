from django.db import models
# En este caso practico se importa el modelo AbstractUser para crear nuestro modelo de Usuario
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)