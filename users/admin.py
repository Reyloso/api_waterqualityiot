from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import (CustomUserCreationForm, CustomUserChangeForm)
from .models import *

# Register your models here.


class Usuarios(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = (
        (None, {'fields': ( 'username','password')}),
        ('Information', {'fields': ('type_user','date_joined','last_login',)}),
        ('Permissions', {'fields': ('user_permissions','groups','is_active','is_superuser','is_admin')}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'type_user', 'username', 'password1', 'password2','user_permissions','groups','is_active','is_superuser','is_admin')}
        ),
    )

    list_filter = ('type_user',)
    search_fields = ('id','username','type_user',)
    list_display = ['id','type_user','username','date_joined','last_login']

    class Meta:
        model = User


class Staffs(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    """ admin para las personas """


    fieldsets = (
        (None, {'fields': ('email', 'username','password')}),
        ('Information personal', {'fields': ('name','first_surname','second_surname','address','city','country','department','phone',)}),
        ('Information account', {'fields': ('type_user','status','date_joined','last_login',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser','groups','user_permissions')}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type_user','email', 'username', 'password1', 'password2','name','first_surname','second_surname','country','department','city','phone','is_superuser','is_staff','is_active','status', 'groups','user_permissions')}
        ),
    )

    list_filter = ('status','is_active','type_user','is_superuser')
    search_fields = ('id','username','email','name', 'first_surname', 'first_surname')
    list_display = ['id','type_user','username','email','name', 'first_surname', 'status', 'is_active','created_at', 'updated_at', 'deleted_at']


    class Meta:
        model = Staff



admin.site.register(User,Usuarios)
admin.site.register(Staff,Staffs)