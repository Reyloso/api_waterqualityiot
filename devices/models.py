from django.db import models
from django.utils import timezone
from users.models import (User, Staff)
from configurations.models import (Country, Department, City)
from django.db.models.signals import post_save
# autoditoria 
from crum import get_current_user

from django.forms import model_to_dict
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
    mac_code = models.CharField(unique=True, max_length=100, null=False, blank=False)
    publish_key_pubnub = models.CharField(max_length=100, null=True, blank=True)
    suscribe_key_pubnub = models.CharField(max_length=100, null=True, blank=True)
    uuid_key_pubnub = models.CharField(max_length=100, null=True, blank=True)
    channel_pubnub = models.CharField(max_length=100, null=True, blank=True)
    staff_created = models.ForeignKey(User, related_name = 'device_staff_created' ,on_delete=models.PROTECT, null=True, blank=True)
    staff_updated = models.ForeignKey(User, related_name = 'device_staff_updated' ,on_delete=models.PROTECT, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name + " " + self.mac_code)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if  not self.pk:
                self.staff_created = user
            else:                
                self.staff_updated = user
        super(Device, self).save(*args, **kwargs)        

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login', 'groups'])
        item['city'] = self.city.toJSON()

        return item

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
    
