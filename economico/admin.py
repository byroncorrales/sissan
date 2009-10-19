from django.contrib import admin
from economico.models import *

class MercadoAdmin(admin.ModelAdmin):
    pass
class SectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}
class CanastaBasicaAdmin(admin.ModelAdmin):
    pass
class SalarioNominalAdmin(admin.ModelAdmin):
    pass
class SalarioRealAdmin(admin.ModelAdmin):
    pass
class SalarioMinimoAdmin(admin.ModelAdmin):
    pass
class FuerzaTrabajoAdmin(admin.ModelAdmin):
    pass
class TipoCanastaBasicaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tipo",)}


admin.site.register(Mercado, MercadoAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(CanastaBasica, CanastaBasicaAdmin)
admin.site.register(SalarioNominal, SalarioNominalAdmin)
admin.site.register(SalarioMinimo, SalarioMinimoAdmin)
admin.site.register(SalarioReal, SalarioRealAdmin)
admin.site.register(FuerzaTrabajo, FuerzaTrabajoAdmin)
admin.site.register(TipoCanastaBasica, TipoCanastaBasicaAdmin)
