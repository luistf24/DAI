from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from .models import Receta, Ingrediente
from .forms import RecetaForm

# Create your views here.

def index(request):

    if request.GET.get('busqueda') != None: 
        busquedas = Receta.objects.filter(nombre = request.GET.get('busqueda') )
        ingredientes = Ingrediente.objects.filter(receta = busquedas[0] )
        return render(request, 'lista_recetas_extend.html', {'busquedas': busquedas, 'ingredientes': ingredientes})

    elif request.GET.get('delete_receta') != None:
        Receta.objects.filter(nombre=request.GET.get('delete_receta')).delete()
        messages.info(request, 'La receta ha sido borrada')
        return redirect('index')

    else:
        busquedas = Receta.objects.all()

        return render(request, 'lista_recetas.html', {'busquedas': busquedas})

def new_receta(request):

    messages.success(request, 'Profile details updated.')
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)

        if form.is_valid():
            receta  = form.instance
            receta.save()
            
            messages.info(request, 'La receta ha sido añadida')
            return redirect('index')

    else:
        form = RecetaForm()

    return render(request, 'receta_new.html', {'form': form})

def edit_receta(request):
    receta = get_object_or_404(Receta.objects.filter(nombre=request.GET.get('edit_receta')))
    
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)

        if form.is_valid():
            receta  = form.instance
            receta.save()
            
            messages.info(request, 'La receta ha sido editada')
            return redirect('index')

    else:
        form = RecetaForm(instance=receta)

    return render(request, 'receta_new.html', {'form': form})
