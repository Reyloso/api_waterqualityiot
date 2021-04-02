from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import admin

# Create your views here.
@login_required
def home(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Inicio',})
	return render(request,'base/home.html', context)



def devices_list(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Dispositivos',})
	return render(request,'devices/devices_list.html', context)

	
def devices_new(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Nuevo Dispositivo',})
	return render(request,'devices/new_device.html', context)


def users_list(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Usuarios',})
	return render(request,'users/users_list.html', context)

def users_new(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Nuevo Usuario',})
	return render(request,'users/users_new.html', context)


def groups_list(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Grupos',})
	return render(request,'users/group_list.html', context)

	
def group_new(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Nuevo Grupo',})
	return render(request,'users/group_new.html', context)


def device_list_measurement(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Seleccionar Dispositivo',})
	return render(request,'measurements/devices_list.html', context)

def measurement_view(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Mediciones De Dispositivo',})
	return render(request,'measurements/view_measurement.html', context)