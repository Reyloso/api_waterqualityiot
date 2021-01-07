from django.contrib import admin
from .models import *
# Register your models here.

class Measurements(admin.ModelAdmin):

    list_filter = ('status','device','country','department','city')
    search_fields = ('id','device__name','name', )
    list_display = ['id','name','device','name', 'status','staff_created','latitude','longitude','created_at', 'updated_at', 'deleted_at']


    class Meta:
        model = Measurement

class data_measurements(admin.ModelAdmin):

    list_filter = ('device',)
    search_fields = ('id','device__name', )
    list_display = ['id','ph','tds','turbidez','temperatura','conductividad','measurement','device','latitude','longitude','created_at', 'updated_at', 'deleted_at']


    class Meta:
        model = Data_measurement

admin.site.register(Measurement, Measurements)
admin.site.register(Data_measurement, data_measurements)