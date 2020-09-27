from django.urls import path
from . views import nueva_queja, carga_municipios

urlpatterns = [
    path('add/', nueva_queja, name='nueva_queja'),
    path('ajax/municipios/', carga_municipios, name='carga_muni'),  # AJAX
]