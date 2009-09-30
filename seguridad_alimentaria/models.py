from django.db import models
import datetime
from lugar.models import Departamento

ANO_CHOICES=[]
for i in range (datetime.date.today().year,1989,-1):
	ANO_CHOICES.append((i,str(i)))
#disp y consumo aparente

class Producto(models.Model):
    nombre = models.CharField("Nombre del Producto", max_length=20)

    def __unicode__(self):
        return self.nombre

#class DisponibilidadConsumo(models.Model):
#    ano = models.IntegerField("Ano", max_length=4, choices=ANO_CHOICES)
#    producto = models.ForeignKey(Producto)
#    disponibilidad = models.DecimalField(max_digits=10, decimal_places=2)
#    consumo_aparente= models.DecimalField(max_digits=10, decimal_places=2)

 #   def __unicode__(self):
 #      return "%s (%s)" % (self.producto.nombre, self.ano)

 #   class Meta:
 #       unique_together=['ano','producto']
 #       ordering=['ano', 'producto']
 #       verbose_name = "Disponibilidad y consumo aparente"
 #       verbose_name_plural = verbose_name

#class DependenciaAlimentaria(models.Model):
#    ano = models.IntegerField("Ano", max_length=4, choices=ANO_CHOICES)
#    producto = models.ForeignKey(Producto)
#    donaciones = models.DecimalField(max_digits=10, decimal_places=2)
#    importaciones = models.DecimalField(max_digits=10, decimal_places=2)

class SoberaniaAlimentaria(models.Model):
    ano = models.IntegerField("Ano", max_length=4, choices=ANO_CHOICES)
    producto = models.ForeignKey(Producto)
    donaciones = models.DecimalField(max_digits=10, decimal_places=2)
    importaciones = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.DecimalField(max_digits=10, decimal_places=2)
    consumo_aparente= models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return "%s (%s)" % (self.producto.nombre, self.ano)

    class Meta:
        unique_together=['ano','producto']
        ordering=['ano', 'producto']
        verbose_name = "Soberania Alimentaria"
        verbose_name_plural = verbose_name

class UtilizacionBiologica(models.Model):
    ano = models.IntegerField("Ano", max_length=4, choices=ANO_CHOICES)
    departamento = models.ForeignKey(Departamento)
    enfermedades_diarreicas = models.DecimalField("Enfermedades diarreicas agudas", max_digits=10, decimal_places=2)
    enfermedades_respiratorias = models.DecimalField("Enfermedades respiratorias agudas", max_digits=10, decimal_places=2)

    def __unicode__(self):
        return "Utilizacion bioligica dept: %s (%s)" % (self.departamento.nombre, self.ano)

    class Meta:
        unique_together=['ano','departamento']
        ordering=['ano']
        verbose_name = "Utilizacion Biologica"
        verbose_name_plural = verbose_name
