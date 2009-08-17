# -*- coding: UTF-8 -*-
from django.db import models
import datetime

CHOICESANO=[]
for i in range (datetime.date.today().year,1989,-1):
	CHOICESANO.append((i,str(i)))

CHOICESMES = (
    (1, 'Enero'),(2, 'Febrero'),(3, 'Marzo'),(4, 'Abril'),(5, 'Mayo'),(6, 'Junio'),(7, 'Julio'),(8, 'Agosto'),(9, 'Septiembre'), (10, 'Octubre'),(11, 'Noviembre'),(12, 'Diciembre')
)

class Exportacion(models.Model):
	ano = models.IntegerField("Ano",max_length=5, choices=CHOICESANO, help_text='Introduzca el ano')
	mes = models.IntegerField("Mes",max_length=2, choices=CHOICESMES, help_text='Introduzca el mes')
	fob = models.DecimalField("FOB",max_digits=10,decimal_places=2)

	class Meta:
		ordering = ['ano']
		unique_together = ['ano','mes']
		verbose_name_plural = "Indicador de Exportaciones de Mercancias FOB"

	#def __unicode__(self):
	#	return self.ano
