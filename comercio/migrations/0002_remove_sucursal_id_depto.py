# Generated by Django 2.2.16 on 2020-09-05 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='id_depto',
        ),
    ]
