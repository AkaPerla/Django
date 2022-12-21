from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo/',views.nuevo,name='nuevo',),
    path('nuevo/nuevoregistro/',views.nuevoregistro,name='nuevoregistro'),
    path('borrar/<int:identificador>',views.borrar,name='borrar'),
    path('modifica/<int:identificador>',views.modifica,name='modifica',),
    path('modifica/modificaregistro/<int:identificador>',views.modificaregistro,name='modificaregistro'),
]