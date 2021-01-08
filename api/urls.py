from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.auth.urls')),
    path('', include('api.configurations.urls')),	
    path('', include('api.devices.urls')),	
    path('', include('api.measurements.urls')),	
    path('', include('api.users.urls')),	
]