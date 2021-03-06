# Generated by Django 2.2.16 on 2020-09-26 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0003_auto_20200905_0056'),
        ('frmqueja', '0003_auto_20200919_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='id_depto',
            field=models.ForeignKey(db_column='id_depto_FK', default=1, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Departamento', verbose_name='Departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='id_muni',
            field=models.ForeignKey(db_column='id_muni_FK', default=1, on_delete=django.db.models.deletion.CASCADE, to='ubicacion.Municipio', verbose_name='Municipio'),
            preserve_default=False,
        ),
    ]
