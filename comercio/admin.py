from django.contrib import admin
from comercio.models import *

# Register your models here

#class SucursalAdmin(admin.ModelAdmin):
#    list_display = ['id_comercio','nombre_sucursal','id_muni','zona','direccion','referencia','telefono']

class ComercioAdmin(admin.ModelAdmin):
    list_display = ['razon_social', 'razon_comercial', 'nit', 'pbx']

admin.site.register (Comercio, ComercioAdmin)
#admin.site.register (Sucursal, SucursalAdmin)