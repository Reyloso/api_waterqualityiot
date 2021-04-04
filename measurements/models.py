from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from devices.models import (Device)
from users.models import (Staff, User)
from configurations.models import (Country, Department, City)

# Create your models here.
class Measurement(models.Model):

    """ modelo para las mediciones """

    status_types = (
        ('Activa', 'Activa'),
        ('Inactiva', 'Inactiva'),
        ('Pausada', 'Pausada'),
    )

    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False, blank=False)
    status = models.CharField(max_length=20, choices=status_types, default='Activa', null=False, blank=False)
    name = models.CharField(max_length=45, null=False, blank=False)
    device = models.ForeignKey(Device, on_delete=models.PROTECT, null=False, blank=False)
    staff_created = models.ForeignKey(User, related_name='mision_staff_created', on_delete=models.PROTECT, null=False, blank=False)
    staff_updated = models.ForeignKey(User, related_name='mision_staff_updated', on_delete=models.PROTECT, null=True, blank=True)
    staff_finished = models.ForeignKey(Staff, related_name='mision_staff_finished', on_delete=models.PROTECT, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Medicion"
        verbose_name_plural = "Mediciones"
        default_permissions = ()
        permissions = (
            ("add_measurement", "Puede guardar mediciones"),
            ("view_measurement", "Puede ver mediciones"),
            ("change_measurement", "Puede actualizar mediciones"),
            ("delete_measurement", "Puede eliminar mediciones"),
        )

    def __str__(self):
        return str("ID:{} |Name:{} | Status: {}".format(self.id, self.name,self.status))


class Data_measurement(models.Model):

    """ modelo para los datos de una medicion """

    ph = models.CharField(_('Potencial de hidrogeno'), max_length=100, null=False, blank=False)
    tds = models.CharField(_('Total solidos disueltos'), max_length=100, null=False, blank=False)
    turbidez = models.CharField(_('Turbidez del agua'), max_length=100, null=False, blank=False)
    temperatura = models.CharField(_('Temperatura del agua'), max_length=100, null=False, blank=False)
    conductividad = models.CharField(_('Conductividad electrica'), max_length=100, null=False, blank=False)
    device = models.ForeignKey(Device, on_delete=models.PROTECT, null=False, blank=False)
    dataJson = models.JSONField(default=dict)
    time = models.CharField( max_length=100, null=False, blank=False)
    measurement = models.ForeignKey(Measurement, on_delete=models.PROTECT, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Data de Medicion"
        verbose_name_plural = "Datos de Mediciones"
        default_permissions = ()
        permissions = (
            ("add_data_measurement", "Puede guardar data de medicion"),
            ("view_data_measurement", "Puede ver data de medicion"),
            ("change_data_measurement", "Puede actualizar data de medicion"),
            ("delete_data_measurement", "Puede eliminar data de medicion"),
        )

    def __str__(self):
        return str("ID:{}".format(self.id))