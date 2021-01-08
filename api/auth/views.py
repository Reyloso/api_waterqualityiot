# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

#models
from users.models import (User, Staff)


################## auth serializers #############
class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)

        return token
    class Meta:
        examples = {
            'username': 'usuario',
            'password': "la contraseña",
        }

class StaffLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'id','type_user', 'name', 'first_surname', 'second_surname',
             'username')

############### auth views ###################
class LoginStaff(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    
    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=False):
            req = request.data
            username = req.get('username')
            password = req.get('password')

            if not username and not password:
                return Response({'code': 2,
                                 'message': 'Los campos nombre de usuario y contraseña faltan o están vacíos',
                                 'data': None},
                                status=200)

            elif not password:
                return Response({'code': 2,
                                 'message': 'Campo contraseña falta o está vacío',
                                 'data': None},
                                status=200)
            elif not username:
                return Response({'code': 2,
                                 'message': 'Campo nombre de usuario falta o está vacío',
                                 'data': None},
                                status=200)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'code': 2,
                                 'message': 'nombre de usuario no existe o es incorrecto',
                                 'data': None},
                                status=200)

            if not user.check_password(password):
                return Response({'code': 2,
                                 'message': 'nombre de usuario o contraseña no existen o son incorrectos',
                                 'data': None},
                                status=200)

            user = User.objects.get(username=username)
            if not user.is_active:
                return Response({'code': 2,
                                 'message': 'Lo sentimos, no te encuentras activo en el sistema',
                                 'data': None},
                                status=200)

        user = User.objects.get(username=request.data.get('username'))
        if user.is_admin:
            return Response({'code': 2,
                             'message': 'Lo sentimos, tienes privilegios de super usuario, debe autenticarse con una cuenta diferente',
                             'data': None},
                            status=200)

        people = Staff.objects.get(username=user.username)
        if not people.status:
            return Response({'code': 2,
                             'message': 'Lo sentimos, no te encuentras activo en el sistema',
                             'data': None},
                            status=200)

        if user.type_user != 'Staff':
            return Response({'code': 2,
                             'message': 'Lo sentimos, no tienes privilegios para acceder a esta aplicación',
                             'data': None},
                            status=200)

        user.last_login = timezone.now()
        user.save()
        response = super(LoginStaff, self).post(request, *args, **kwargs)
        res = response.data
        token = res.get('access')
        userinfo = StaffLoginSerializer(people)
        return Response({'code': 1,
                         'message': 'Inicio de sesión exitoso',
                         'data': token,
                         'infouser': userinfo.data},
                        status=200)