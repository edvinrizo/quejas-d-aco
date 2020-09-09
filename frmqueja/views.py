from django.shortcuts import render

# Create your views here.
def quejas_diaco(request):
    return render(request, 'frmqueja/quejas.html', {})