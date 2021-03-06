# Generated by Django 2.2.16 on 2020-09-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frmqueja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='apellido_cliente',
            field=models.CharField(blank=True, db_column='apellido', max_length=50, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='factura',
            field=models.CharField(db_column='factura', max_length=50, verbose_name='Factura'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='id_sucursal',
            field=models.ForeignKey(db_column='id_sucursal_FK', on_delete='CASCADE', to='comercio.Sucursal', verbose_name='Sucursal'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='nombre_cliente',
            field=models.CharField(blank=True, db_column='nombre', max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='formulario',
            name='solicitud',
            field=models.TextField(db_column='solcitud', verbose_name='Solicitud'),
        ),
    ]
