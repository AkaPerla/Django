from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from .models import Receta
# Create your views here.
def inicio(request):
    home = loader.get_template('recetario/inicio.html')
    return HttpResponse(home.render())

def receta(request):
    receta = Receta.object.latest('created')
    
    ctx = {
        'receta': receta,
    }
    
    receta = loader.get_template('recetario/receta.html')
    return HttpResponse(receta.render(ctx.request))

def desayunos(request):
    recetas = Receta.object.filter(categorias__nombre='Desayuno')
    
    ctx = {
        'recetas': recetas,
    }
    
    todas = loader.get_template('recetario/desayunos.html')
    return HttpResponse(todas.render(ctx,request))

def comidas(request):
    comidas = loader.get_template('recetario/comidas.html')
    return HttpResponse(comidas.render())

def cenas(request):
    cenas = loader.get_template('recetario/cenas.html')
    return HttpResponse(cenas.render())

def todas(request):
    
    recetas = get_list_or_404(Receta)
    
    ctx = {
        'recetas': recetas,
    }
    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render(ctx,request))

def categoria(request,idCategoria):
    recetas = get_list_or_404(Receta, categorias=idCategoria)
    ctx = {
        'recetas': recetas,
    }
    todas = loader.get_template('recetario/todas.html')
    return HttpResponse(todas.render(ctx,request))