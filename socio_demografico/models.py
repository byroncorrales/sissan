# -*- coding: UTF-8 -*-
from django.db import models
import datetime

CHOICESQUINQUENIO = (
    ('1950-1955', '1950-1955'),('1955-1960','1955-1960'),('1960-1965','1960-1965'),('1965-1970', '1965-1970'),('1970-1975', '1970-1975'),('1975-1980', '1975-1980'),('1980-1985', '1980-1985'),('1985-1990', '1985-1990'),('1990-1995', '1990-1995'),('1995-2000', '1995-2000'),( '2000-2005', '2000-2005'),('2005-2010', '2005-2010'),('2010-2015', '2010-2015'),('2015-2020', '2015-2020'),('2020-2025', '2020-2025'),('2025-2030', '2025-2030'),('2030-2035', '2030-2035'),('2035-2040', '2035-2040'),('2040-2045', '2040-2045'),('2045-2050', '2045-2050'),('2050-2055', '2050-2055')
)

CHOICESANO=[]
for i in range (datetime.date.today().year,1959,-1):
	CHOICESANO.append((i,str(i)))

class Crecimiento(models.Model):
	ano = models.CharField("Quinquenio", choices=CHOICESQUINQUENIO, max_length=12, help_text='Introduzca el quinquenio', unique=True)
	crecimiento = models.DecimalField("Tasa de crecimiento poblacional (%)",max_digits=10,decimal_places=2)

	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Tasa de crecimiento"

class Esperanza(models.Model):
	ano = models.CharField("Quinquenio", choices=CHOICESQUINQUENIO, max_length=12, help_text='Introduzca el quinquenio', unique=True)
	ambos_sexos = models.DecimalField("Total ambos sexos",max_digits=10,decimal_places=2, editable=False)
	mujer = models.DecimalField("Mujer",max_digits=10,decimal_places=2)
	hombre = models.DecimalField("Hombre",max_digits=10,decimal_places=2)
	
	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Esperanza de vida"
	
	def save(self, force_insert=False, force_update=False):
		self.ambos_sexos = self.hombre + self.mujer
		super(Esperanza,self).save(force_insert, force_update)

class Fecundidad(models.Model):
	ano = models.CharField("Quinquenio", choices=CHOICESQUINQUENIO, max_length=12, help_text='Introduzca el quinquenio', unique=True)
	fecundidad = models.DecimalField("Fecundidad, No hijos por mujer",max_digits=10,decimal_places=2)
	natalidad = models.DecimalField("Tasa bruta natalidad",max_digits=10,decimal_places=2)
	
	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Fecundidad"
		
class Mortalidad_materna(models.Model):
	ano = models.IntegerField("Año",max_length=5, choices=CHOICESANO, help_text='Introduzca el año', unique=True)
	mortalidad = models.DecimalField("Tasa mortalidad materna", max_digits=10, decimal_places=2)
	
	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Mortalidad Materna"
		
class Mortalidad_infantil(models.Model):
	ano = models.IntegerField("Año",max_length=5, choices=CHOICESANO, help_text='Introduzca el año', unique=True)
	mortalidad = models.DecimalField("Tasa mortalidad minfantil", max_digits=10, decimal_places=2)
	mortalidad_menor = models.DecimalField("Tasa mortalidad infantil < 5 años", max_digits=10, decimal_places=2)
	
	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Mortalidad Infantil"
