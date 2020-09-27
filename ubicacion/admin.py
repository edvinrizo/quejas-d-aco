from django.contrib import admin
from ubicacion.models import *

# Register your models here.
class RegionAdmin (admin.ModelAdmin):
    list_display = ['nombre_region']
    list_filter = ['id_region']

class MunicipioInline(admin.TabularInline):
    model = Municipio
    extra = 2
    #list_display = ['nombre_muni']
    #list_filter = ['id_muni']

class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [MunicipioInline]
    list_display = ['nombre_depto']
    list_filter = ['id_region']
    search_fields = ['nombre_depto']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre_muni']
    list_filter = ['id_depto']

admin.site.register(Region, RegionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio)