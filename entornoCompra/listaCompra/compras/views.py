from django.http import HttpResponse
from django.shortcuts import render
from .models import Compras
from django.template import loader
# Create your views here.
def compras(request):
    lc = Compras.objects.all()
    context = {
        'compras':lc,
    }
    plantilla = loader.get_template('compras.html')
    return HttpResponse(plantilla.render(context,request))