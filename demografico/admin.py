from django.contrib import admin
from demografico.models import Poblacion

class PoblacionAdmin(admin.ModelAdmin):
	list_display = ['ano','departamento','total_ambos_sexos', 'total_hombre', 'total_mujer', 'urbano_ambos_sexos', 'rural_ambos_sexos','densidad']
	list_filter = ['ano']
	#search_fields = ['departamento']

admin.site.register(Poblacion, PoblacionAdmin)



