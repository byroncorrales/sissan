# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import Departamento

CHOICESANO = (
    (1990, '1990'),(1991, '1991'),(1992, '1992'),(1993, '1993'),(1994, '1994'),(1995, '1995'),(1996, '1996'),(1997, '1997'),(1998, '1998'),(1999, '1999'),(2000, '2000'),(2001, '2001'),(2002, '2002'),(2003, '2003'),(2004, '2004'),(2005, '2005'),(2006, '2006'),(2007, '2007'),(2008, '2008'),(2009, '2009'),(2010, '2010'),(2011, '2011'),(2012, '2012'),(2013, '2013'),(2014, '2014'),(2015, '2015'),(2016, '2016'),(2017, '2017'),(2018, '2018'),(2019, '2019'),(2020, '2020'),(2021, '2021'),(2022, '2022'),(2023, '2023'),(2024, '2024'),(2025, '2025'),(2026, '2026'),(2027, '2027'),(2028, '2028'),(2029, '2029'),(2030, '2030')
)

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
        
        def save(self, force_insert=False, force_update=False):
                self.rural_ambos_sexos = self.rural_hombre + self.rural_mujer
                self.urbano_ambos_sexos = self.urbano_hombre + self.urbano_mujer
                self.total_hombre = self.rural_hombre + self.urbano_hombre
                self.total_mujer = self.rural_mujer + self.urbano_mujer
                self.total_ambos_sexos = self.total_hombre + self.total_mujer
                super(Poblacion,self).save(force_insert, force_update)

	



