from django.db import models
from django.utils import timezone
from django.forms import model_to_dict
# Create your models here.
# models type departament
class Country(models.Model):

    """ modelo para los paises """

    name = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item
        
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        default_permissions = ()
        permissions = (
            ("add_country", "Puede guardar paises"),
            ("view_country", "Puede ver paises"),
            ("change_country", "Puede actualizar paises"),
            ("delete_country", "Puede eliminar paises"),
        )

    def __str__(self):
        return str("ID: {} | Name: {} ".format(self.id, self.name))

# models type departament
class Department(models.Model):
    """ modelo para los departamentos """

    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        default_permissions = ()
        permissions = (
            ("add_department", "Puede guardar departamentos"),
            ("view_department", "Puede ver departamentos"),
            ("change_department", "Puede actualizar departamentos"),
            ("delete_department", "Puede eliminar departamentos"),
        )

    def __str__(self):
        return str("ID: {} | Name: {} ".format(self.id, self.name))


# ciudades
class City(models.Model):
    """ modelo para los ciudades """

    department = models.ForeignKey(Department, on_delete=models.PROTECT,null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        default_permissions = ()
        permissions = (
            ("add_city", "Puede guardar ciudades"),
            ("view_city", "Puede ver ciudades"),
            ("change_city", "Puede actualizar ciudades"),
            ("delete_city", "Puede eliminar ciudades"),
        )

    def __str__(self):
        return str("ID: {} | Name: {} | Departament: {}".format(self.id, self.name,self.department))
