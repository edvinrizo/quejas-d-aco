from django.urls import path
from . import views

urlpatterns = [
    path('', views.quejas_diaco, name='quejas_diaco'),
]