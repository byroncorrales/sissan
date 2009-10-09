from django.db import models

class Departamento(models.Model):
    id = models.IntegerField("Numero de dept", primary_key=True)
    slug = models.SlugField(unique=True, null=True)
    nombre = models.CharField(max_length=30)
    extension = models.DecimalField("Extension Territorial", max_digits=10,decimal_places=2)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"

class Municipio(models.Model):
    id = models.IntegerField("Numero de dept", primary_key=True)
    departamento = models.ForeignKey(Departamento)
    nombre = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=True)
    extension = models.DecimalField("Extension Territorial", max_digits=10, decimal_places=2, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Municipios"

