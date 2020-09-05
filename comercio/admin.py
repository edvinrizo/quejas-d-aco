from django.contrib import admin
from comercio.models import *

# Register your models here.
class TipoComercioAdmin (admin.ModelAdmin):
    list_display = ['tipo_comercio']

class SucursalInline(admin.TabularInline):
    model = Sucursal
    extra = 1
    list_display = ['id_comercio','nombre_sucursal','id_muni','zona','direccion','referencia','telefono']

class ComercioAdmin(admin.ModelAdmin):
    inlines = [SucursalInline]
    list_display = ['razon_social', 'razon_comercial', 'nit', 'pbx']

admin.site.register (TipoComercio, TipoComercioAdmin)
admin.site.register (Comercio, ComercioAdmin)
admin.site.register (Sucursal)