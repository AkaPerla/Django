from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Socios
from django.urls import reverse
def index(request):
  socios = Socios.objects.all().values()
  template = loader.get_template('interfazSocio.html')
  contexto = {
    'listaSocios':socios,
  }
  return HttpResponse(template.render(contexto,request))
  
  # socios = Socios.objects.all().values()
  # output = ""
  # for x in socios:
  #   output += "_"+ x["nombre"] + " "+x["apellidos"]
  # return HttpResponse(output)
  
def nuevo(request):
  template =loader.get_template('nuevoSocio.html')
  return HttpResponse(template.render({},request))

def nuevoregistro(request):
  n = request.POST['nombre']
  a = request.POST['apellidos']
  socio= Socios(nombre=n,apellidos=a)
  socio.save()
  return HttpResponseRedirect(reverse('index'))

def borrar(request,identificador):
  socio = Socios.objects.get(id=identificador)
  socio.delete()
  return HttpResponseRedirect(reverse('index'))

def modifica(request, identificador):
  socio = Socios.objects.get(id=identificador)
  template = loader.get_template('modifica.html')
  contexto = {
    'socio': socio,
  }
  return HttpResponse(template.render(contexto, request))

def modificaregistro(request, identificador):
  nombre = request.POST['nombre']
  apellidos = request.POST['apellidos']
  socio = Socios.objects.get(id=identificador)
  socio.nombre = nombre
  socio.apellidos = apellidos
  socio.save()
  return HttpResponseRedirect(reverse('index'))