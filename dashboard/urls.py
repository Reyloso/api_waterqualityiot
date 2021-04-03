from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), 
            name='login'),
          
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('', views.home, name='home'),
    path('devices/', views.devices_list, name='devices-list'),
    path('devices/new', views.devices_new, name='devices-new'),

    path('measurement/', views.device_list_measurement, name='measurement-select'),
    path('measurement/view', views.measurement_view, name='measurement-view'),

    path('users/', views.users_list, name='user-list'),
    path('users/new', views.users_new, name='user-new'),

    path('group/', views.groups_list, name='groups-list'),
    path('group/new', views.group_new, name='group-new'),
    # path('mis_posts', views.mis_posts, name='mis_posts'),
    # path('categorias', views.categorias, name='categorias'),
    # path('detalle_post/<int:pk>', views.detalle_post),

    # Country
    path('country/list', views.CountryListView.as_view(), name='country_list'),
    path('country/add/', views.CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', views.CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/', views.CountryDeleteView.as_view(), name='country_delete'),
]