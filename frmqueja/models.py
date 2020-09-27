from django.db import models
from comercio.models import *
from ubicacion.models import *

# Create your models here.


class Formulario (models.Model):
    objects = models.Manager()
    id_frmqueja = models.AutoField('Id Queja', primary_key=True, db_column='id_frmqueja_PK', editable=False)
    fecha_registro = models.DateField('Fecha Queja', auto_now=True, db_column='fecha_registro', editable=False)
    nombre_cliente = models.CharField('Nombre', db_column='nombre', null=True, blank=True,
                                      max_length=50)
    apellido_cliente = models.CharField('Apellido', db_column='apellido', null=True, blank=True,
                                        max_length=50)
    fecha_incidente = models.DateField('Fecha del Incidente', auto_now=False, db_column='fecha_incidente')
    factura = models.CharField('Factura', max_length=50, db_column='factura')
    id_comercio = models.ForeignKey(Comercio, verbose_name='Comercio', db_column='id_comercio_FK', on_delete=models.CASCADE)
    #id_sucursal = models.ForeignKey(Sucursal, verbose_name='Sucursal', db_column='id_sucursal_FK', on_delete=models.CASCADE)
    detalle_queja = models.TextField('Detalle de la queja', db_column='detalle_queja')
    solicitud = models.TextField('Solicitud', db_column='solcitud')
    region = models.CharField('Region', editable=False, db_column='region', max_length=25, null=True, blank=True)
    id_depto = models.ForeignKey(Departamento, verbose_name='Departamento', db_column='id_depto_FK', on_delete=models.CASCADE)
    id_muni = models.ForeignKey(Municipio, verbose_name='Municipio', db_column='id_muni_FK', on_delete=models.CASCADE)
    nombre_sucursal = models.CharField('Sucursal', db_column='nombre_sucursal', max_length=200)
    zona = models.IntegerField('Zona', db_column='zona')
    direccion = models.CharField('dirección', db_column='direccion', max_length=250)
    referencia = models.CharField('Referencia', db_column='referencia', max_length=400, blank=True, null=True)
    telefono = models.CharField('Telefono', max_length=10, db_column='telefono', null=True, blank=True)

    def __str__(self):
        return '%s' % (self.detalle_queja)

    class Meta:
        verbose_name = 'queja'
        verbose_name_plural = 'quejas'
        db_table = 'tbl_formulario'


