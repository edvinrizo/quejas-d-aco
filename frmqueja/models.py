from django.db import models
from comercio.models import Sucursal

# Create your models here.


class Formulario (models.Model):
    id_frmqueja = models.IntegerField('Id Queja', primary_key=True, db_column='id_frmqueja_PK', editable=False)
    fecha_registro = models.DateField('Fecha Queja', auto_now=True, db_column='fecha_registro', editable=False)
    nombre_cliente = models.CharField('Nombre', help_text='Opcional', db_column='nombre', null=True, blank=True,
                                      default='Anónimo', max_length=50)
    apellido_cliente = models.CharField('Apellido', help_text='Opcional', db_column='apellido', null=True, blank=True,
                                        default='Anónimo', max_length=50)
    fecha_incidente = models.DateField('Fecha del Incidente', auto_now=False, db_column='fecha_incidente')
    factura = models.CharField('Factura', max_length=50, db_column='factura', help_text='No. de factura del comercio')
    id_sucursal = models.ForeignKey(Sucursal, verbose_name='Sucursal', db_column='id_sucursal_FK', on_delete='CASCADE',
                                    help_text='Ingrese datos del comercio')
    detalle_queja = models.TextField('Detalle de la queja', db_column='detalle_queja')
    solicitud = models.TextField('Solicitud', db_column='solcitud', help_text='Explique su sugerencia o solicitud')

    def __str__(self):
        return '%s' % (self.id_frmqueja)

    class Meta:
        verbose_name = 'queja'
        verbose_name_plural = 'quejas'
        db_table = 'tbl_formulario'


