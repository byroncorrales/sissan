from django.contrib import admin
from lugar.models import Departamento, Municipio

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['numero','nombre']
        list_filter = ['nombre']
        search_fields = ['nombre']


admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio)




