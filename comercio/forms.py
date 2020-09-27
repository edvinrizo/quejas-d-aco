from django import forms
from django.forms import TextInput, Select

from .models import Comercio
from ubicacion.models import *


class ComercioForm(forms.ModelForm):

    class Meta:
        model = Comercio
        fields = [
            'razon_social',
            'razon_comercial',
            'nit',
            'pbx',
        ]

        widgets = {
            'razon_social': TextInput(attrs={'placeholder': 'Este campo es opcional'}),
            'razon_comercial': TextInput(attrs={'placeholder': 'Nombre del Comercio'}),
            'nit': TextInput(attrs={'placeholder': 'Nit del comercio, sin guión (-), solo números'}),
            'pbx': TextInput(attrs={'placeholder': 'Número Telefónico'}),
        }


#class SucursalForm(forms.ModelForm):
#
#    class Meta:
#        model = Sucursal
#        fields = '__all__'
#
#        def __init__(self, *args, **kwargs):
#            super().__init__(*args, **kwargs)
#            self.fields['id_muni'].queryset = Municipio.objects.none()
#
#           if 'id_depto' in self.data:
#              try:
#                    depto_id = int(self.data.get('id_depto'))
#                    self.fields['id_muni'].queryset = Municipio.objects.filter(depto_id=depto_id).order_by('nombre_depto')
#                except (ValueError, TypeError):
#                    pass  # invalid input from the client; ignore and fallback to empty City queryset
#            elif self.instance.pk:
#                self.fields['id_muni'].queryset = self.instance.id_depto.id_muni_set.order_by('nombre_muni')
#
#
#       widgets = {
#            'id_comercio': Select(attrs={'placeholder': 'Seleccione el Comercio'}),
#            'nombre_sucursal': TextInput(attrs={'placeholder': 'Ingrese nombre de la sucursal'}),
#            #'id_depto': Select(attrs={'placeholder': 'Seleccione un departamento'}),
#            #'id_muni': Select(attrs={'placeholder': 'Seleccione un municipio'}),
#            'zona': TextInput(attrs={'placeholder': 'Ingrese Zona'}),
#            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
#            'referencia': TextInput(attrs={'placeholder': 'Aquí puede colocar una referencia de la ubicación'}),
#            'telefono': TextInput(attrs={'placeholder': 'Número Telefónico'}),
#        }