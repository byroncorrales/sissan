# -*- coding: UTF-8 -*-
from django.db import models

CHOICESANO = (
    (1990, '1990'),(1991, '1991'),(1992, '1992'),(1993, '1993'),(1994, '1994'),(1995, '1995'),(1996, '1996'),(1997, '1997'),(1998, '1998'),(1999, '1999'),(2000, '2000'),(2001, '2001'),(2002, '2002'),(2003, '2003'),(2004, '2004'),(2005, '2005'),(2006, '2006'),(2007, '2007'),(2008, '2008'),(2009, '2009'),(2010, '2010'),(2011, '2011'),(2012, '2012'),(2013, '2013'),(2014, '2014'),(2015, '2015'),(2016, '2016'),(2017, '2017'),(2018, '2018'),(2019, '2019'),(2020, '2020'),(2021, '2021'),(2022, '2022'),(2023, '2023'),(2024, '2024'),(2025, '2025'),(2026, '2026'),(2027, '2027'),(2028, '2028'),(2029, '2029'),(2030, '2030')
)

CHOICESMES = (
    (1, 'Enero'),(2, 'Febrero'),(3, 'Marzo'),(4, 'Abril'),(5, 'Mayo'),(6, 'Junio'),(7, 'Julio'),(8, 'Agosto'),(9, 'Septiembre'), (10, 'Octubre'),(11, 'Noviembre'),(12, 'Diciembre')
)

class Exportacion(models.Model):
	ano = models.IntegerField("Ano",max_length=5, choices=CHOICESANO, help_text='Introduzca el ano')
        mes = models.IntegerField("Mes",max_length=2, choices=CHOICESMES, help_text='Introduzca el mes')
	fob = models.DecimalField("FOB",max_digits=10,decimal_places=2)
        
	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Indicador de Exportaciones de Mercancias FOB"

	#def __unicode__(self):
	#	return self.ano
