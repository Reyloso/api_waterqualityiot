from django.urls import path

from .views import *

urlpatterns = [ 
    path('api/report/data', ReportByData_measurementApi.as_view()),
    # path('api/measurements/data/bull/create', DataMeasurementeBullCreatedView.as_view()),
    # path('api/measurements/data/<int:pk>', MeasurementeListView.as_view())
]