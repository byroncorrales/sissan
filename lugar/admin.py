from django.contrib import admin
from lugar.models import Departamento, Municipio

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['numero','nombre','extension']
	list_filter = ['nombre']
	search_fields = ['nombre']

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ['numero','nombre','departamento']
	list_filter = ['departamento']
	search_fields = ['nombre']

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)




