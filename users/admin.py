from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import (CustomUserCreationForm, CustomUserChangeForm)
from .models import *

# Register your models here.


class Usuarios(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Information', {'fields': ('type_user','date_joined','last_login',)}),
        ('Permissions', {'fields': ()}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'type_user','email', 'username', 'password1', 'password2')}
        ),
    )

    list_filter = ('type_user',)
    search_fields = ('id','email','username','type_user',)
    list_display = ['id','type_user','username', 'email','date_joined','last_login']

    class Meta:
        model = User


# admin.site.register(User,Usuarios)