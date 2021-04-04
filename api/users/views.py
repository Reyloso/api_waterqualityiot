# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group, Permission
from django.utils import timezone
from django.db.models import F
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import (SerializerRol, SerializerPermisos)
from ..query import (filtro_roles)

from ..permissions import IsAuthenticated

#vista de roles
class RolLista(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = SerializerRol
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = Group.objects.all()
        queryset = self.filter_queryset(query)

        group = filtro_roles(queryset, **request.query_params)
        serializer = SerializerRol(group['items'], many=True)
        result = dict()
        result['message'] = 'Lista de Roles'
        result['code'] = 1
        result['data'] = serializer.data
        result['draw'] = group['draw']
        result['recordsTotal'] = group['total']
        result['recordsFiltered'] = group['count']

        if serializer:
            return Response(result, status=200, template_name=None, content_type=None)
        else:
            result = dict()
            result['message'] = 'Lista de Roles'
            result['code'] = 1
            result['data'] = None
            result['draw'] = 0
            result['recordsTotal'] = 0
            result['recordsFiltered'] = 0
            return Response(result, status=200, template_name=None, content_type=None)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors, 'code': 5, 'data': None}
            return Response(data, status=400)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'message': 'Registro guardado con éxito', 'code': 1, 'data': serializer.data}
        return Response(data, status=200, headers=headers)


#vista de detalle de rol
class RolDetalle(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = SerializerRol
    http_method_names = ['get','put']
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk):
        queryset = Group.objects.get(pk=pk)
        serializer = SerializerRol(queryset)

        if serializer:
            data = {'message': 'detalle de rol', 'code': 1, 'data': serializer.data}
            return Response(data, status=200)
        else:
            data = {'message': 'detalle de rol', 'code': 1, 'data': None}
            return Response(data, status=200)

    def put(self, request, pk):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors, 'code': 5, 'data': None}
            return Response(data, status=400)

        serializer.save()
        data = {'message': 'Registro actualizado con éxito', 'code': 1, 'data': serializer.data}
        return Response(data, status=200)

#vista de lista de permisos
class ListaPermisos(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = SerializerPermisos
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        query = Permission.objects.all()
        serializer = self.get_serializer(query, many=True)

        if serializer:
            data = {'message': 'Lista de permisos', 'code': 1, 'data': serializer.data}
            return Response(data, status=200)
        else:
            data = {'message': 'Lista de permisos', 'code': 1, 'data': []}
            return Response(data, status=200)        