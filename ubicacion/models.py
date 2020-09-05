from django.db import models

# Create your models here.
class Region (models.Model):
    id_region = models.IntegerField('No. Region', db_column='id_region_PK', primary_key=True, editable=False)
    nombre_region = models.CharField('Region', help_text='Ingrese: Norte, Centro, Sur, Oriente, Occidente', max_length=25,
                              db_column='nombre_region', unique=True)

    def __str__(self):
        return self.nombre_region

    class Meta:
        verbose_name = 'region'
        verbose_name_plural = 'regiones'
        db_table = 'tbl_region'

class Departamento (models.Model):
    id_depto = models.IntegerField('Id Departamento', db_column='id_depto_PK', primary_key=True, editable=False)
    nombre_depto = models.CharField('Departamento', db_column='nombre_depto', max_length=50, unique=True)
    id_region = models.ForeignKey(Region, verbose_name='Region', db_column='id_region_FK', on_delete='CASCADE')

    def __str__(self):
        return self.nombre_depto

    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'
        db_table = 'tbl_depto'

class Municipio (models.Model):
    id_muni = models.IntegerField('Id Municipio', db_column='id_muni_PK', primary_key=True, editable=False)
    nombre_muni = models.CharField('Municipio', db_column='nombre_muni', max_length=50)
    id_depto = models.ForeignKey(Departamento, verbose_name='Departamento', db_column='id_depto_FK', on_delete='CASCADE')

    def __str__(self):
        return self.nombre_muni

    class Meta:
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
        db_table = 'tbl_muni'