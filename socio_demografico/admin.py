from django.contrib import admin
from socio_demografico.models import Crecimiento, Esperanza, Fecundidad, Mortalidad_materna, Mortalidad_infantil

class CrecimientoAdmin(admin.ModelAdmin):
	list_display = ['ano','crecimiento']
	list_filter = ['ano']
     
class EsperanzaAdmin(admin.ModelAdmin):
	list_display = ['ano','ambos_sexos','mujer','hombre']
	list_filter = ['ano']

class FecundidadAdmin(admin.ModelAdmin):
	list_display = ['ano','fecundidad','natalidad']
	list_filter = ['ano']

class Mortalidad_maternaAdmin(admin.ModelAdmin):
	list_display = ['ano','mortalidad']
	list_filter = ['ano']

class Mortalidad_infantilAdmin(admin.ModelAdmin):
	list_display = ['ano','mortalidad','mortalidad_menor']
	list_filter = ['ano']

admin.site.register(Crecimiento, CrecimientoAdmin)
admin.site.register(Esperanza, EsperanzaAdmin)
admin.site.register(Fecundidad, FecundidadAdmin)
admin.site.register(Mortalidad_materna, Mortalidad_maternaAdmin)
admin.site.register(Mortalidad_infantil, Mortalidad_infantilAdmin)
