from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from dashboard.forms import CountryForm
# Models
from configurations.models import Country
# Create your views here.
@login_required
def home(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Inicio',})
	return render(request,'base/home.html', context)

# Listar ciudad
class CountryListView(ListView):
    model = Country
    template_name = 'configurations/country/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Country.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
		
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciudades'
        context['create_url'] = reverse_lazy('country_create')
        return context

# Crear ciudad
class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'configurations/country/create.html'
    success_url = reverse_lazy('country_list')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de pais '
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('country_list')
        return context
    

# Editar ciudad
class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'configurations/country/create.html'
    success_url = reverse_lazy('country_list')
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de pais '
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('country_list')
        return context


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