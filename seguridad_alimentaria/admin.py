from django.contrib import admin
from seguridad_alimentaria.models import *

class ProductoAdmin(admin.ModelAdmin):
    pass
class SoberaniaAlimentariaAdmin(admin.ModelAdmin):
    pass
class UtilizacionBiologicaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Producto, ProductoAdmin)
admin.site.register(SoberaniaAlimentaria, SoberaniaAlimentariaAdmin)
admin.site.register(UtilizacionBiologica, UtilizacionBiologicaAdmin)
