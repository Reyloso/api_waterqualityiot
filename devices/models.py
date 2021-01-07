from django.db import models
from django.utils import timezone
from users.models import (User, Staff)
from configurations.models import (Country, Department, City)
from django.db.models.signals import post_save
# Create your models here.


class Device(User):
    """ clase device que hereda de la clase user"""

    status_types = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    status_device = models.CharField(max_length=20, choices=status_types, default='Activo', null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False, blank=False)
    name = models.CharField(unique=True, max_length=100, null=False, blank=False)
    imei_code = models.CharField(unique=True, max_length=100, null=False, blank=False)
    staff_created = models.ForeignKey(Staff, related_name = 'device_staff_created' ,on_delete=models.PROTECT, null=False, blank=False)
    staff_updated = models.ForeignKey(Staff, related_name = 'device_staff_updated' ,on_delete=models.PROTECT, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name + " " + self.imei_code)

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"
        default_permissions = ()
        permissions = (
            ("add_device", "Puede guardar device"),
            ("view_device", "Puede ver device"),
            ("change_device", "Puede actualizar device"),
            ("delete_device", "Puede eliminar device"),
        )
    
