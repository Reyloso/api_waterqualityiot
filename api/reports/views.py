# -*- coding: utf-8 -*-
from rest_framework import generics
from django.db import connection
from django.db.models import (Max, Min)
import io

from api.permissions import (IsAuthenticated)
from rest_framework.response import Response

from api.reports.xls import generateXls


from measurements.models import Data_measurement

# reporte de ventas generales
class ReportByData_measurementApi(generics.ListAPIView):
    """ 
    get:

    ejemplo de filtros: ?date_start=10-08-2020&date_end=11-08-2020

    campos de filtro

    date_start : tipo fecha , date_end: tipo fecha
    
    """

    queryset = Data_measurement.objects.filter(deleted_at=None)
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            report_name = 'General Data'

            
            created_at = Data_measurement.objects.filter(deleted_at=None).aggregate(createdMin=Min('created_at'),
                                                                        createdMax=Max('created_at'))

            if 'date_start' in request.query_params:
                date_start = request.query_params['date_start']
            else:
                date_start = created_at['createdMin'].strftime("%d-%m-%Y")

            if 'date_end' in request.query_params:
                date_end = request.query_params['date_end']
            else:
                date_end = created_at['createdMax'].strftime("%d-%m-%Y")

            if 'export' in request.query_params:
                export = request.query_params['export']
            else:
                export = None
            
            print(date_end)
            print(date_start)

            cursor = connection.cursor()
            cursor.execute("set datestyle to SQL,DMY; "
                "    SET datestyle = dmy; "
                "    select mdm.ph as ph, "
                "    mdm.tds as tds,  "
                "    mdm.turbidez,  "
                "    mdm.temperatura, "
                "    mdm.conductividad, "
                "    mdm.time as fecha "
                "    from measurements_data_measurement mdm where "
                "    to_char( to_date(mdm.time,'MM DD YYYY'), 'DD-MM-YYYY' )::DATE BETWEEN '{0}'::DATE  "
                " AND '{1}'::DATE  order by to_char( to_date(mdm.time,'MM DD YYYY'), 'DD-MM-YYYY' )::DATE".format(str(date_start), str(date_end)))

            queryJson = []
            for row in cursor.fetchall():
                queryJson.append({
                    'ph': row[0],
                    'tds': row[1],
                    'turbidez': row[2],
                    'temperatura': row[3],
                    'conductividad': row[4],
                    'fecha': row[5]
                })

            header_keys = [{'PH':'text'},{'TDS':'text'},{'Turbidez':'text'},{'Temperatura':'text'},{'Conductividad':'text'},
                            {'Fecha':'text'}]

            model_name = self.queryset.model.__name__
            if queryJson and (export == None or export ==''):
                data = {'message': '{}'.format(report_name), 'code': 1, 'data': queryJson}
                return Response(data, status=200)
            elif queryJson and export == 'xls':
                response =  generateXls(report_name, queryJson, header_keys=header_keys)
                return response
            else:
                data = {'message': 'Lo sentimos, no se encontraron resultados en esta busqueda', 'code': 2, 'data': []}
                return Response(data, status=200)
        except Exception as e:
            data = {'message': str(e), 'code': 2, 'data': None}
            return Response(data, status=400)
