from django.shortcuts import render, HttpResponse
from .models import Receta

# Create your views here.

def index(request):

    if request.GET.get('busqueda') != None: 
        busquedas = Receta.objects.filter(nombre = request.GET.get('busqueda') )

        return render(request, 'lista_recetas_extend.html', {'busquedas': busquedas})

    else:
        busquedas = Receta.objects.all()

        return render(request, 'lista_recetas.html', {'busquedas': busquedas})

