# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import Departamento
import datetime

CHOICESANO=[]
for i in range (datetime.date.today().year,1959,-1):
	CHOICESANO.append((i,str(i)))
	
class Poblacion(models.Model):
	ano = models.IntegerField("Año",max_length=5, choices=CHOICESANO, help_text='Introduzca el año')
	departamento = models.ForeignKey(Departamento,help_text='Introduzca nombre del departamento')
	total_ambos_sexos = models.IntegerField("Total de ambos sexos",max_length=10, editable=False)
	total_hombre = models.IntegerField("Total hombres",max_length=10, editable=False)
	total_mujer = models.IntegerField("Total mujer",max_length=10, editable=False)
	urbano_ambos_sexos = models.IntegerField("Ambos sexos urbano",max_length=10, editable=False)
	urbano_hombre = models.IntegerField("Hombre urbano",max_length=10)
	urbano_mujer = models.IntegerField("Mujer urbano",max_length=10)
	rural_ambos_sexos = models.IntegerField("Ambos sexos rural",max_length=10, editable=False)
	rural_hombre = models.IntegerField("Hombre rural",max_length=10)
	rural_mujer = models.IntegerField("Mujer rural",max_length=10)
	
        class Meta:
		ordering = ['ano']
		verbose_name_plural = "Indicador de Poblacion"
		unique_together = ['ano','departamento']

        def save(self, force_insert=False, force_update=False):
                self.rural_ambos_sexos = self.rural_hombre + self.rural_mujer
                self.urbano_ambos_sexos = self.urbano_hombre + self.urbano_mujer
                self.total_hombre = self.rural_hombre + self.urbano_hombre
                self.total_mujer = self.rural_mujer + self.urbano_mujer
                self.total_ambos_sexos = self.total_hombre + self.total_mujer
                super(Poblacion,self).save(force_insert, force_update)

	



