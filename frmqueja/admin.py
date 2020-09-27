from django.contrib import admin
from frmqueja.models import *
from django.http import HttpResponse
from xlwt.compat import xrange
import xlwt
from rangefilter.filter import DateRangeFilter


class FormularioAdmin(admin.ModelAdmin):

    def export_xls(modeladmin, request, queryset):

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=quejas.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Quejas")

        row_num = 0

        columns = [
            (u"Queja", 15000),
            (u"Sugerencia", 15000),
            (u"Sucursal", 8000),
            (u"Comercio", 8000),
            (u"No. Factura", 3000),
            (u"Fecha de Incidente", 3000),
            (u"Fecha de Registro", 3000),
            (u"Nombre Cliente", 3000),
            (u"Apellido Cliente", 3000),
        ]

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1

        for obj in queryset:
            row_num += 1
            row = [
                obj.detalle_queja,
                obj.solicitud,
                obj.id_sucursal.nombre_sucursal,
                obj.id_comercio.razon_comercial,
                obj.factura,
                obj.fecha_incidente,
                obj.fecha_registro,
                obj.nombre_cliente,
                obj.apellido_cliente,
            ]
            for col_num in xrange(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

    export_xls.short_description = u"Export XLS"
    actions = [export_xls]
    list_display = ['detalle_queja','solicitud','nombre_sucursal','id_comercio','factura','fecha_incidente','fecha_registro',
                    'nombre_cliente','apellido_cliente', 'region', 'id_depto', 'id_muni']
    search_fields = ['nombre_cliente', 'apellido_cliente', 'factura', 'nombre_sucursal', 'id_comercio__razon_comercial',
                     'id_depto__nombre_depto', 'id_muni__nombre_muni']
    list_filter = (
        ('fecha_registro', DateRangeFilter), ('fecha_incidente',DateRangeFilter), 'id_depto__nombre_depto', 'region')

admin.site.register(Formulario, FormularioAdmin)

