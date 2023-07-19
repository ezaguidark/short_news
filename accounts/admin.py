from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Fields que se muestran en la lista de usuarios
    list_display = ['email', 'username', 'is_staff', ]

    # Fields que se muestran al editar el modelo
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'profile_image', 'description', 'title', 'waifu', 'website', 'github', 'linkedin', )}),
    )
    # Fields que se muestran al crear un usuario nuevo desde admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'profile_image', 'description', 'title', 'waifu', 'website', 'github', 'linkedin',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)