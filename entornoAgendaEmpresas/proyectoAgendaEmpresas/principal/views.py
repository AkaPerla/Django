# from http.client import HTTPResponse
# from django.shortcuts import render, get_list_or_404
# from django.template import loader
# from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from .models import Empresas
# Create your views here.

class EmpresaListView(ListView):
    model = Empresas

class EmpresaDetailView(DetailView):
    model = Empresas
'''
def listado (request):
    #modelo
    empresas = get_list_or_404(Empresas)
    #contexto
    ctx = {
        'empresas': empresas,
    }
    #template
    listadoHtml = loader.get_template('principal/listado.html')
    #retirn template
    return HttpResponse(listadoHtml.render(ctx,request))
'''   