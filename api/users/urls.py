from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
 
    re_path(r'^roles-lista$', RolLista.as_view()),
    re_path(r'^roles-detalle/(?P<pk>\d+)$', RolDetalle.as_view()),
    re_path(r'^permisos-lista$', ListaPermisos.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)