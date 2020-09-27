from django.shortcuts import render, redirect
from .forms import ComercioForm
from ubicacion.models import *

# Create your views here.

#def nueva_sucursal(request):
#    if request.method == 'POST':
#        form = SucursalForm(request.POST)
#        if form.is_valid():
#            form.save()
#        return redirect('queja:nueva_queja')
#    else:
#        form = SucursalForm()
#    return render(request, 'comercio/add_sucursal.html', {'form': form})


def nuevo_comercio(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('queja:nueva_queja')
    else:
        form = ComercioForm()
    return render(request, 'comercio/add_comercio.html', {'form': form})

# AJAX
def carga_municipios(request):
    depto_id = request.GET.get('depto_id')
    municipio = Municipio.objects.filter(id_depto=depto_id).all()
    return render(request, 'comercio/muni_dropdown_list_options.html', {'municipio': municipio})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)