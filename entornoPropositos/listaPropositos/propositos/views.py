from datetime import datetime, timedelta
from django.shortcuts import render
from .models import ModeloPropositos
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.
def listaPropositos(request):
    fechaActual = datetime.datetime.now().date()
    prop = ModeloPropositos.objects.all()
    context = {
        'propositos':prop,
        'fechaActual':fechaActual,
    }
    plantilla = loader.get_template('propositos.html')
    return HttpResponse(plantilla.render(context,request))

def add(request):
    prop = request.GET['proposito']
    fechaOb = request.GET['fechaObjetivo']
    proposito = ModeloPropositos(proposito=prop,fechaObjetivo=fechaOb,conseguido=False)
    proposito.save()
    
    return HttpResponseRedirect(reverse('listaPropositos'))

def borrar(request,identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    prop.delete()
    return HttpResponseRedirect(reverse('listaPropositos'))

def modificar(request, identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    context = {
        'modPropositos':prop
    }
    plantilla = loader.get_template('modificar.html')
    return HttpResponse(plantilla.render(context,request))

def actualizar (request,identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    prop.proposito = request.GET['proposito']
    prop.save()
    return HttpResponseRedirect(reverse('listaPropositos'))

def modificarFecha(request, identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    context = {
        'modPropositos':prop
    }
    plantilla = loader.get_template('modificarFecha.html')
    return HttpResponse(plantilla.render(context,request))

def actualizarFecha(request,identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    dias = int(request.GET['fechaActualizada'])
    if dias > 0:
        prop.fechaObjetivo = prop.fechaObjetivo - (-1*(timedelta(days=dias)))
        prop.save()
    return HttpResponseRedirect(reverse('listaPropositos'))

def conseguido(request,identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    prop.fechaConseguido = datetime.datetime.now()
    prop.conseguido = True
    prop.save()
    return HttpResponseRedirect(reverse('listaPropositos'))

def resetear(request,identificador):
    prop = ModeloPropositos.objects.get(id=identificador)
    prop.fechaConseguido = None
    prop.conseguido = False
    prop.save()
    return HttpResponseRedirect(reverse('listaPropositos'))