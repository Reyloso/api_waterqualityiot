# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

from rest_framework import permissions


class IsAuthenticated(BasePermission):
    """
        La solicitud se autentica utilizando los permisos `django.contrib.auth`.
        Consulte: https://docs.djangoproject.com/en/dev/topics/auth/#permissions
        Asegura que el usuario está autenticado, y tiene la adecuada
        `create` / `list` / `update` / `delete` permisos en el modelo.
        Este permiso solo se puede aplicar a las clases de vista que
        proporcionar un atributo `.queryset`.
        """
    #
    # Mapear los métodos en los códigos de permiso requeridos.
    # Anule esto si también necesita proporcionar permisos de 'visualización'
    # o si desea proporcionar códigos de permiso personalizados.
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def get_required_permissions(self, method, model_cls):
        """
            Dado un modelo y un método HTTP, devuelve la lista de permisos
            que el usuario debe tener.
        """
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }

        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        return [perm % kwargs for perm in self.perms_map[method]]

    def _queryset(self, view):
        assert hasattr(view, 'get_queryset') \
               or getattr(view, 'queryset', None) is not None, (
            'Cannot apply {} on a view that does not set '
            '`.queryset` or have a `.get_queryset()` method.'
        ).format(self.__class__.__name__)

        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
            assert queryset is not None, (
                '{}.get_queryset() returned None'.format(view.__class__.__name__)
            )
            return queryset
        return view.queryset

    def has_permission(self, request, view):
        authenticated = bool(request.user and request.user.is_authenticated)

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        return authenticated and request.user.has_perm(perms[0])
