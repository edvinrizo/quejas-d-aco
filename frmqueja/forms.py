from django import forms
from django.forms import TextInput, Textarea, Select, DateInput, DateField

from .models import Formulario
from ubicacion.models import *

class DateInput(forms.DateInput):
    input_type = 'date'
    format= '%d-%m-%Y'

class QuejasForm(forms.ModelForm):

    class Meta:
        model = Formulario
        fields = [
            'id_comercio',
            'nombre_sucursal',
            'id_depto',
            'id_muni',
            'direccion',
            'zona',
            'referencia',
            'telefono',
            'factura',
            'fecha_incidente',
            'detalle_queja',
            'solicitud',
            'nombre_cliente',
            'apellido_cliente',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['id_muni'].queryset = Municipio.objects.none()

            if 'id_depto' in self.data:
                try:
                    depto_id = int(self.data.get('id_depto'))
                    self.fields['id_muni'].queryset = Municipio.objects.filter(depto_id=depto_id).order_by('nombre_depto')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['id_muni'].queryset = self.instance.id_depto.id_muni_set.order_by('nombre_muni')

        widgets = {
            'id_comercio': Select(attrs={'placeholder': 'Seleccione Comercio'}),
            'nombre_sucursal': TextInput(attrs={'placeholder': 'Ingrese Sucursal'}),
            'id_depto': Select(attrs={'placeholder': 'Seleccione Departamento'}),
            'id_muni': Select(attrs={'placeholder': 'Seleccione Municipio'}),
            'factura': TextInput(attrs={'placeholder': 'Número de factura'}),
            'fecha_incidente': DateInput(format=('%d/%m/%Y')),
            'detalle_queja': Textarea(attrs={'placeholder': 'Describa aquí su queja'}),
            'solicitud': Textarea(attrs={'placeholder': 'En este espacio puede indicar si tiene una sugerencia para '
                                                         'solucionar el problema'}),
            'nombre_cliente': TextInput(attrs={'placeholder': 'Este campo es opcional'}),
            'apellido_cliente': TextInput(attrs={'placeholder': 'Este campo es opcional'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'zona': TextInput(attrs={'placeholder': 'Ingrese la zona'}),
            'referencia': TextInput(attrs={'placeholder': 'Ingrese una referencia para la dirección'}),
            'telefono': TextInput(attrs={'placeholder': 'Ingrese un número de telefono'}),
        }