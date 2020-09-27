from django.shortcuts import render, redirect
from .forms import QuejasForm
from ubicacion.models import Municipio


# Create your views here.
def quejas_diaco(request):
    return render(request, 'frmqueja/quejas.html')


def nueva_queja(request):
    if request.method == 'POST':
        form = QuejasForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('queja:nueva_queja')
    else:
        form = QuejasForm()
    return render(request, 'frmqueja/queja_edit.html', {'form': form})


# AJAX
# def carga_sucursales(request):
#    comercio_id = request.GET.get('comercio_id')
#    sucursal = Sucursal.objects.filter(id_comercio=comercio_id).all()
#    return render(request, 'frmqueja/sucursal_dropdown_list_options.html', {'sucursal': sucursal})
#    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def carga_municipios(request):
    depto_id = request.GET.get('depto_id')
    municipio = Municipio.objects.filter(id_depto=depto_id).all()
    return render(request, 'frmqueja/muni_dropdown_list_options.html', {'municipio': municipio})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
