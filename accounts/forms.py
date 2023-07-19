from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser # el modelo que creamos con los datos que queremos
        fields = ('username','email' ,) # cambiar el form del signup

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email' ,'age', 'profile_image',
            'description', 'title', 'waifu', 'website',
            'github', 'linkedin',
        )