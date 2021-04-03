from django.urls import path

from .views import *

urlpatterns = [ path('api/measurements/data/create', DataMeasurementeCreatedView.as_view()),]