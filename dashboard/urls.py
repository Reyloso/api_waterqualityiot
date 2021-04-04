from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), 
            name='login'),
          
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', views.home, name='home'),

    # Dispositivos
    path('devices/list', views.DevicesListView.as_view(), name='devices_list'),    
    path('devices/add/', views.DevicesCreateView.as_view(), name='devices_create'),
    path('devices/update/<int:pk>/', views.DevicesUpdateView.as_view(), name='devices_update'),
    path('devices/delete/<int:pk>/', views.DevicesDeleteView.as_view(), name='devices_delete'),


    # Mediciones
    path('measurement/list', views.MeasurementsListView.as_view(), name='measurements_list'),
    path('measurement/add/', views.MeasurementsCreateView.as_view(), name='measurement_create'),
    path('measurement/update/<int:pk>/', views.MeasurementsUpdateView.as_view(), name='measurement_update'),
    path('measurement/delete/<int:pk>/', views.MeasurementsDeleteView.as_view(), name='measurement_delete'),

    path('devices/new', views.devices_new, name='devices-new'),

    path('measurement/', views.device_list_measurement, name='measurement-select'),

    path('measurement/view/<int:pk>', views.measurement_view, name='measurement-view'),

    # Usuarios
    path('users/', views.users_list.as_view(), name='user_list'),
    path('users/add/', views.Users_new.as_view(), name='user_create'),
    path('users/update/<int:pk>/', views.UserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='users_delete'),

    # Grupos y roles
    # path('groups/list', views.GroupsListView.as_view(), name='groups_list'),
    path('groups/add/', views.group_new, name='groups_create'),

    path('groups/list', views.inicioRoles, name='group_list'),

    # Country
    path('country/list', views.CountryListView.as_view(), name='country_list'),
    path('country/add/', views.CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', views.CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/', views.CountryDeleteView.as_view(), name='country_delete'),

    # Departamentos
    path('department/list', views.DepartmentListView.as_view(), name='department_list'),    
    path('department/add/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('department/update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('department/delete/<int:pk>/', views.DepartmentDeleteView.as_view(), name='department_delete'),


    # Ciudades
    path('city/list', views.CityListView.as_view(), name='city_list'),    
    path('city/add/', views.CityCreateView.as_view(), name='city_create'),
    path('city/update/<int:pk>/', views.CityUpdateView.as_view(), name='department_update'),
    path('city/delete/<int:pk>/', views.CityDeleteView.as_view(), name='city_delete'),
]