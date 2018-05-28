from django.contrib import admin
from django_divipola_colombia import models
# Register your models here.

admin.site.register(models.Departamentos)
admin.site.register(models.Municipios)
admin.site.register(models.CentrosPoblados)