from django.shortcuts import redirect, render
from ordenamiento.models import Parroquia, Barrio
from ordenamiento.forms import ParroquiaForm, BarrioForm, BarrioParroquiaForm


def index(request):
    parroquias = Parroquia.objects.all()

    informacion_template = {'Parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)


def listadoParroquias(request):
  
    parroquias = Parroquia.objects.all()
    
    informacion_template = {'parroquias': parroquias}
    return render(request, 'listadoParroquias.html', informacion_template)

def listadoBarrios(request):
    
    barrios = Barrio.objects.all()
   
    informacion_template = {'barrios': barrios,  'numero_barrios' : len(barrios)}
    return render(request, 'listadoBarrios.html', informacion_template)
    

def crearParroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario) 


def crearBarrioParroquia(request, id):

    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'estudiante': parroquia}

    return render(request, 'crearBarrioParroquia.html', diccionario) 


def editarParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 

def editarBarrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario) 