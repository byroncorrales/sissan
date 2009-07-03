 # -*- coding: UTF-8 -*-

from django.db import models

class Departamento(models.Model):
	nombre = models.CharField(max_length=30)
	numero = models.DecimalField(decimal_places=0,max_digits=2,primary_key=True)			
	
        class Meta:
            verbose_name_plural = "Departamentos"

	def __unicode__(self):
             return self.nombre
        
class Municipio(models.Model):
	nombre = models.CharField(max_length=30)		
	departamento = models.ForeignKey(Departamento)
        
        class Meta:
            verbose_name_plural = "Municipios"

	def __unicode__(self):
             return self.nombre
