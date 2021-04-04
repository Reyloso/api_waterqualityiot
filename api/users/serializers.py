# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from django.db import transaction
from ..query import (filtro_roles)

# Rol 
class SerializerRol(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class SerializerPermisos(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = ('id', 'name')


class SerializerRolMin(serializers.ModelSerializer):
    # groups = SerializerRolMin(read_only=True)

    class Meta:
        model = Group
        fields =  ('id','name')
