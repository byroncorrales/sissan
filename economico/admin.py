from django.contrib import admin
from economico.models import Exportacion

class ExportacionAdmin(admin.ModelAdmin):
	list_display = ['ano','mes','fob']
	list_filter = ['ano']
	#search_fields = ['departamento']

admin.site.register(Exportacion, ExportacionAdmin)
