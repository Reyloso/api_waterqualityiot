from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from dashboard.forms import CountryForm, DepartmentForm, CityForm, UserForm, DeviceForm,MeasurementsForm
from django.utils import timezone
from django.utils import timezone as tz
from datetime import date

from datetime import datetime

# Models
from configurations.models import Country, Department, City
from users.models import Staff
from devices.models import Device
from measurements.models import Measurement

# Create your views here.
@login_required
def home(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Inicio',})
	return render(request,'base/home.html', context)

# Listar ciudad
class CountryListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
                for i in Country.objects.filter(deleted_at=None):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
		
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Paises'
        context['create_url'] = reverse_lazy('country_create')
        return context

# Crear pais
class CountryCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
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
    

# Editar pais
class CountryUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
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

# Eliminar pais
class CountryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Country
    template_name = 'configurations/country/delete.html'
    success_url = reverse_lazy('country_list')

    def dispatch(self, request, *args, **kwargs):
        # asignamos la instancia a esta variable para luego usarla
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            
            # aqui la tiene el objeto la instancia
            instance = self.object
            instance.deleted_at = timezone.now()
            instance.save()
            # self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un pais'
        context['list_url'] = self.success_url
        return context



# Listar departamento
class DepartmentListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Department
    template_name = 'configurations/department/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Department.objects.filter(deleted_at=None).order_by('-created_at'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
		
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Departamentos'
        context['create_url'] = reverse_lazy('department_create')
        return context



# Crear departamento
class DepartmentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Department
    form_class = DepartmentForm
    template_name = 'configurations/department/create.html'
    success_url = reverse_lazy('department_list')
    
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
        context['titulo'] = 'Creacion de departamento '
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('department_list')
        return context
    


# Editar departamento
class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Department
    form_class = DepartmentForm
    template_name = 'configurations/department/create.html'
    success_url = reverse_lazy('department_list')

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
        context['titulo'] = 'Edicion de departamento '
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('department_list')
        return context


# Eliminar departamento
class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Department
    template_name = 'configurations/department/delete.html'
    success_url = reverse_lazy('department_list')

    def dispatch(self, request, *args, **kwargs):
        # asignamos la instancia a esta variable para luego usarla
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            
            # aqui la tiene el objeto la instancia
            instance = self.object
            instance.deleted_at = timezone.now()
            instance.save()
            # self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un departamento'
        context['list_url'] = self.success_url
        return context



# Listar ciudad
class CityListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = City
    template_name = 'configurations/city/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in City.objects.filter(deleted_at=None).order_by('-created_at'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
		
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciudades'
        context['create_url'] = reverse_lazy('city_create')
        return context


# Crear ciudad
class CityCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = City
    form_class = CityForm
    template_name = 'configurations/country/create.html'
    success_url = reverse_lazy('city_list')
    
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
        context['titulo'] = 'Creacion de ciudad '
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('city_list')
        return context
    

# Editar ciudad
class CityUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = City
    form_class = CityForm
    template_name = 'configurations/country/create.html'
    success_url = reverse_lazy('city_list')

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
        context['titulo'] = 'Edicion de ciudad '
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('city_list')
        return context


# Eliminar ciudad
class CityDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = City
    template_name = 'configurations/city/delete.html'
    success_url = reverse_lazy('city_list')

    def dispatch(self, request, *args, **kwargs):
        # asignamos la instancia a esta variable para luego usarla
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            
            # aqui la tiene el objeto la instancia
            instance = self.object
            instance.deleted_at = timezone.now()
            instance.save()
            # self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminación de un departamento'
        context['list_url'] = self.success_url
        return context



def devices_list(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Dispositivos',})
	return render(request,'devices/devices_list.html', context)

	
def devices_new(request):
	context = admin.site.each_context(request)
	context.update({'titulo': 'Nuevo Dispositivo',})
	return render(request,'devices/new_device.html', context)

# listado de usuarios Staff
class users_list(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Staff
    template_name = 'users/users_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print(action)
            if action == 'searchdata':
                data = []
                for i in Staff.objects.filter(deleted_at=None).order_by('-created_at'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['create_url'] = reverse_lazy('user_create')
        context['list_url'] = reverse_lazy('user_list')
        return context


# Creacion de usuarios Staff
class Users_new(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Staff
    form_class = UserForm
    template_name = 'users/users_new.html'
    success_url = reverse_lazy('user_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
        context['titulo'] = 'Creación de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


# Editar Usuario Staff         
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    form_class = UserForm
    template_name = 'users/users_new.html'
    success_url = reverse_lazy('user_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
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
        context['titulo'] = 'Edición de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

#Eliminar usaurio
class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    template_name = 'users/users_delete.html'
    success_url = reverse_lazy('user_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminación de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        return context


# listado dispositivos
class DevicesListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Device
    template_name = 'devices/devices_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Device.objects.filter(deleted_at=None).order_by('-created_at'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de dispositivos'
        context['create_url'] = reverse_lazy('devices_create')
        context['list_url'] = reverse_lazy('devices_list')
        return context


# Creacion de dispositivo
class DevicesCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Device
    form_class = DeviceForm
    template_name = 'devices/new_device.html'
    success_url = reverse_lazy('devices_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
        context['titulo'] = 'Creación de dispositivos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


# Editar dispositivo          
class DevicesUpdateView(LoginRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'devices/new_device.html'
    success_url = reverse_lazy('devices_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
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
        context['titulo'] = 'Edición de un dispositivo'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


# Eliminar Dispositivo
class DevicesDeleteView(LoginRequiredMixin, DeleteView):
    model = Device
    template_name = 'devices/delete.html'
    success_url = reverse_lazy('devices_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminación de un Dispositivo'
        context['list_url'] = self.success_url
        return context


# listado Mediciones
class MeasurementsListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Measurement
    template_name = 'measurements/list_measurement.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Measurement.objects.filter(deleted_at=None).order_by('-created_at'):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de mediciones'
        context['create_url'] = reverse_lazy('measurement_create')
        context['list_url'] = reverse_lazy('measurements_list')
        return context



# Creacion de Mediciones
class MeasurementsCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Measurement
    form_class = MeasurementsForm
    template_name = 'measurements/new_measurements.html'
    success_url = reverse_lazy('measurements_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
        context['titulo'] = 'Creación de mediciones'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context



# Editar MEdicion          
class MeasurementsUpdateView(LoginRequiredMixin, UpdateView):
    model = Measurement
    form_class = MeasurementsForm
    template_name = 'measurements/new_measurements.html'
    success_url = reverse_lazy('measurements_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
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
        context['titulo'] = 'Edición de una mediciono'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context



# Eliminar departamento
class MeasurementsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Measurement
    template_name = 'measurements/delete_measurements.html'
    success_url = reverse_lazy('measurements_list')

    def dispatch(self, request, *args, **kwargs):
        # asignamos la instancia a esta variable para luego usarla
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            
            # aqui la tiene el objeto la instancia
            instance = self.object
            instance.deleted_at = timezone.now()
            instance.save()
            # self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una medicion'
        context['list_url'] = self.success_url
        return context




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