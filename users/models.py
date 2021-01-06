  # Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, AbstractUser, PermissionsMixin)
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator
from configurations.models import (Country, Department, City)
# Create your models here.

class UserManagers(BaseUserManager):
    """ clase abstracta de usuario para extender el modelo usuario """

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Debe tener un nombre de usuario')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        uother_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        user.save(using=self._db)
        return user


# super class user
class User(AbstractBaseUser, PermissionsMixin):
    """ clase usuario que hereda de la clase abstracta user manager """

    type_users = (
        ('OWNER', 'OWNER'),
        ('STAFF', 'STAFF'),
        ('COMERCIAL', 'COMERCIAL'),
    )
    
    username = models.CharField(_('username'), max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(_('email addres'), max_length=255, unique=True, blank=False, null=False)
    type_user = models.CharField(max_length=20, choices=type_users, default='OWNER', null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManagers()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        default_permissions = ()
        permissions = (
            ("add_user", "Puede guardar usuarios"),
            ("view_user", "Puede ver usuarios"),
            ("change_user", "Puede actualizar usuarios"),
            ("delete_user", "Puede eliminar usuarios"),
        )

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username



# class staff hereda de user
class Staff(User):
    """ clase starr que hereda de la clase user"""

    # type_document = models.ForeignKey(TypeDocument, on_delete=models.PROTECT, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    first_surname = models.CharField(max_length=100, null=False, blank=False)
    second_surname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=5000, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def full_name(self):
        return str(self.name + " " + self.first_surname)

    class Meta:
        verbose_name = "staff"
        verbose_name_plural = "staffs"
        default_permissions = ()
        permissions = (
            ("add_staff", "Puede guardar staff"),
            ("view_staff", "Puede ver staff"),
            ("change_staff", "Puede actualizar staff"),
            ("delete_staff", "Puede eliminar staff"),
        )
    