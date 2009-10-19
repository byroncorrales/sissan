from django.contrib import admin
from lugar.models import Departamento, Municipio

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','extension']
    list_filter = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ['nombre']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','departamento']
    list_filter = ['departamento']
    search_fields = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)




