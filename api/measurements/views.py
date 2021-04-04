
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.db import transaction
from django.utils import timezone
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from api.permissions import (IsAuthenticated)

#websocket
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
channel_layer = get_channel_layer()

from measurements.models import (Data_measurement, Measurement)
from devices.models import Device

from api.query import filtro_dataMeasurement


class DataMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_measurement
        fields = fields = ('id','ph','tds', 'turbidez','temperatura','conductividad','device','measurement', 'time')


class DataMeasurementeCreatedView(generics.ListCreateAPIView):
    queryset = Data_measurement.objects.filter(deleted_at=None)
    serializer_class = DataMeasurementSerializer
    http_method_names = ['post','get']
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        device = Device.objects.filter(id=request.user.id)
        try:
            if device:
                device = device.last()
                measurement = Measurement.objects.filter(device=device, status='Activa', deleted_at=None)
                serializer = self.get_serializer(data=request.data)
                if measurement:
                    measurement = measurement.last()

                    data = Data_measurement(ph=request.data['Ph'],tds=request.data['tds'],turbidez=request.data['turbidez'],
                    temperatura=request.data['temp'],conductividad=request.data['tds'], time=request.data['date_time'], 
                    device=device,measurement=measurement, created_at=timezone.now())
                    data.save()
                    
                else:
                    data = Data_measurement(ph=request.data['Ph'],tds=request.data['tds'],turbidez=request.data['turbidez'],
                    temperatura=request.data['temp'],conductividad=request.data['tds'], time=request.data['date_time'], 
                    device=device, dataJson=request.data, created_at=timezone.now())
                    data.save()
                serializer = DataMeasurementSerializer(data)
                try :
                    async_to_sync(channel_layer.group_send)(
                        str(device.id),
                        {
                            'type': 'send_data',
                            'message': "data enviada",
                            'code': 1,
                            'data': serializer.data
                        }
                    )
                except Exception:
                    e = sys.exc_info()[1]
                    data = {'message': e.args[0], 'code': 2, 'data':None}

                data = {'message': 'Registro guardado con éxito', 'code': 1, 'data': None}
            else:
                data = {'message': 'usted no es un usuario valido para esta opcion', 'code': 2, 'data': None}
        except Exception:
            e = sys.exc_info()[1]
            data = {'message':e.args[0], 'code': 2, 'data':None}

        return Response(data=data, status=200)


class MeasurementeListView(generics.ListCreateAPIView):
    queryset = Data_measurement.objects.filter(deleted_at=None)
    serializer_class = DataMeasurementSerializer
    http_method_names = ['post','get']
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        query = Data_measurement.objects.filter(device_id=pk).order_by('-id')
        queryset = self.filter_queryset(query)
        group = filtro_dataMeasurement(queryset, **request.query_params)
        serializer = DataMeasurementSerializer(group['items'], many=True)
        result = dict()
        result['message'] = 'Lista de mediciones'
        result['code'] = 1
        result['data'] = serializer.data
        result['draw'] = group['draw']
        result['recordsTotal'] = group['total']
        result['recordsFiltered'] = group['count']

        if serializer:
            return Response(result, status=200, template_name=None, content_type=None)
        else:
            result = dict()
            result['message'] = 'Lista de mediciones'
            result['code'] = 1
            result['data'] = None
            result['draw'] = 0
            result['recordsTotal'] = 0
            result['recordsFiltered'] = 0
            return Response(result, status=200, template_name=None, content_type=None)