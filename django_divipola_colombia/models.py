from django.db import models

# Create your models here.

class Departamentos(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre

class Municipios(models.Model):
    departamento = models.ForeignKey(Departamentos, on_delete=models.DO_NOTHING)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)

    class Meta:
        ordering = ['codigo']
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre

class CentrosPoblados(models.Model):
    municipio = models.ForeignKey(Municipios, on_delete=models.DO_NOTHING)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10)
    longitud = models.DecimalField(max_digits=30, decimal_places=20)
    latitud = models.DecimalField(max_digits=30, decimal_places=20)
    tipo_municipio = models.CharField(max_length=20)

    class Meta:
        ordering = ['codigo']
        verbose_name = 'CentroPoblado'
        verbose_name_plural = 'Centros Poblados'

    def __str__(self):
        return self.nombre