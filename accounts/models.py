from django.db import models
# En este caso practico se importa el modelo AbstractUser para crear nuestro modelo de Usuario
from django.contrib.auth.models import AbstractUser
# Se pueden incluir regex en los fields
from django.core.validators import RegexValidator

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default="profile_images/default.jpg")
    description = models.TextField(null=True, blank=True, max_length=250, default="- Description -")
    title = models.CharField(null=True, blank=True, max_length=55, error_messages={
        'max_length': 'Too long uwu'
    }, default="- Title -")
    waifu = models.ImageField(upload_to='profile_images/', null=True, blank=True, default="profile_images/default_waifu.jpg")
    website = models.URLField(null=True, blank=True)
    github = models.URLField(
        null=True, blank=True,
        default="https://github.com/"
    )
    linkedin = models.URLField(
        null=True, blank=True, 
        default="https://www.linkedin.com/in/"
    )
