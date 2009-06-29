from django.db import models

CUENCA_CHOICES=((1,'Sílico Creek parte Alta – Media y Baja'),(2,'Zompopas y Torcuel'),)

class Poblacion(models.Model):
	ano = models.IntegerField(max_length=5,help_text='Introduzca el año')
	total_ambos_sexos = models.IntegerField(max_length=10)
        total_hombre = models.IntegerField(max_length=10)
	total_mujer = models.IntegerField(max_length=10)
	urbano_ambos_sexos = models.IntegerField(max_length=10)
	urbano_hombre = models.IntegerField(max_length=10)
	urbano_mujer = models.IntegerField(max_length=10)
	rural_ambos_sexos = models.IntegerField(max_length=10)
	rural_hombre = models.IntegerField(max_length=10)
	rural_mujer = models.IntegerField(max_length=10)
	class Meta:
		ordering = ['ano']
		verbose_name_plural = "Indicador de Poblacion"

	def __unicode__(self):
		return self.ano
