from django.db import models
from ubicacion.models import *
# Create your models here

class Comercio (models.Model):
    id_comercio = models.AutoField('ID Comercio', primary_key=True, editable=False, db_column='id_comercio_PK')
    razon_social = models.CharField('Razon Social', max_length=100, db_column='razon_social', null=True, blank=True)
    razon_comercial = models.CharField('Razon Comercial', max_length=100, db_column='razon_comercial')
    nit = models.IntegerField('NIT', db_column='nit', unique=True)
    pbx = models.CharField('PBX', db_column='pbx', max_length=10, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.razon_comercial)

    class Meta:
        verbose_name = 'comercio'
        verbose_name_plural = 'comercios'
        db_table = 'tbl_comercio'

#class Sucursal (models.Model):
#    objects = models.Manager()
#    id_sucursal = models.IntegerField('ID Sucursal', db_column='id_sucursal_PK', primary_key=True, editable=False)
#    id_comercio = models.ForeignKey(Comercio, verbose_name='Comercio', db_column='id_comercio_FK', on_delete=models.CASCADE)
#    nombre_sucursal = models.CharField('Sucursal', db_column='nombre_sucursal', max_length=200)
#    id_depto = models.ForeignKey(Departamento, verbose_name='Departamento',
#                                help_text='Departamento donde se ubica el comercio',
#                                 db_column='id_depto_FK', on_delete=models.CASCADE)
#    id_muni = models.ForeignKey(Municipio, help_text='Municipio donde se ubica el comercio', verbose_name='Municipio',
#                               db_column='id_muni_FK', on_delete=models.CASCADE)
#    zona = models.IntegerField('Zona', db_column='zona')
#    direccion = models.CharField('dirección', db_column='direccion', max_length=250)
#    referencia = models.CharField('Referencia', help_text='De una referencia de la ubicación de la sucursal',
#                                  db_column='referencia', max_length=400, blank=True, null=True)
#    telefono = models.CharField('Telefono', max_length=10, db_column='telefono', null=True, blank=True)#
#
#    def __str__(self):
#        return '%s' % (self.nombre_sucursal)
#
#    class Meta:
#        verbose_name = 'sucursal'
#        verbose_name_plural = 'sucursales'
#        db_table = 'tbl_sucursal'
#        unique_together = ('id_comercio', 'nombre_sucursal')
