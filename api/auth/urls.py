from django.urls import path

from .views import *

urlpatterns = [
    path('auth/token/staff', LoginStaff.as_view()),
    path('auth/token/device', LoginDevice.as_view()),
]