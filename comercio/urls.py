from django.urls import path
from . import views

urlpatterns = [
#    path('', views.nueva_sucursal, name='nueva_sucursal'),
    path('comercio/', views.nuevo_comercio, name='nuevo_comercio'),
    path('ajax/municipios/', views.carga_municipios, name='carga_muni'),  # AJAX
]