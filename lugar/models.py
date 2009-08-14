 # -*- coding: UTF-8 -*-

from django.db import models

class Departamento(models.Model):
	numero = models.IntegerField(max_length=10,primary_key=True)
	nombre = models.CharField(max_length=30)
	extension = models.DecimalField("Extension Territorial", max_digits=10,decimal_places=2)
	
	
	class Meta:
		verbose_name_plural = "Departamentos"

	def __unicode__(self):
		return self.nombre

class Municipio(models.Model):
	numero = models.IntegerField(max_length=10,primary_key=True)
	departamento = models.ForeignKey(Departamento)
	nombre = models.CharField(max_length=30)
			
	
        
        class Meta:
            verbose_name_plural = "Municipios"

	def __unicode__(self):
             return self.nombre
