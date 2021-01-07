from django.contrib import admin
from users.forms import (CustomUserCreationForm, CustomUserChangeForm)
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
# Register your models here.

class Devices(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    """ admin para las personas """


    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('Information device', {'fields': ('name','status_device','latitude', 'longitude','city','country','department','imei_code',)}),
        ('Information account', {'fields': ('type_user','status','date_joined','last_login',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser','groups','user_permissions')}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type_user','status_device','username', 'password1', 'password2','name','country','department','city','imei_code','is_superuser','is_staff','is_active','status', 'groups','user_permissions')}
        ),
    )

    list_filter = ('status','is_active','status_device','country','department','city','type_user','is_superuser')
    search_fields = ('id','username','name', )
    list_display = ['id','type_user','username','name','status_device', 'status', 'is_active','created_at', 'updated_at', 'deleted_at']


    class Meta:
        model = Device


admin.site.register(Device, Devices)

