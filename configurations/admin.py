from django.contrib import admin
from .models import *

# Register your models here.
# admin countries
class Countries(admin.ModelAdmin):
    """ admin para los paises """
    list_filter = ('status',)
    search_fields = ('name',)
    list_display = ['id', 'name' ,'status', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = Country

# admin departements
class Departments(admin.ModelAdmin):
    """ admin para los departamentos """

    list_filter = ('status',)
    autocomplete_fields = ['country']
    search_fields = ('name',)
    list_display = ['id', 'name', 'country',  'status', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = Department


# admin cities
class Cities(admin.ModelAdmin):
    """ admin para los ciudades """

    list_filter = ('status',)
    autocomplete_fields = ['department']
    search_fields = ('name',)
    list_display = ['id', 'name', 'department', 'status', 'created_at', 'updated_at', 'deleted_at']

    class Meta:
        model = City

admin.site.register(Country, Countries)
admin.site.register(Department, Departments)
admin.site.register(City, Cities)