from django.urls import path 
from . import views

urlpatterns = [
    path('',views.listaPropositos, name='listaPropositos'),
    path('add', views.add, name='add'),
    path('borrar/<int:identificador>', views.borrar, name='borrar'),
    path('modificar/<int:identificador>', views.modificar, name = 'modificar'),
    path('modificar/actualizar/<int:identificador>',views.actualizar, name='actualizar'),
    path('modificarFecha/<int:identificador>', views.modificarFecha, name = 'modificarFecha'),
    path('modificarFecha/actualizarFecha/<int:identificador>',views.actualizarFecha, name='actualizarFecha'),
    path('conseguido/<int:identificador>',views.conseguido,name='conseguido'),
    path('resetear/<int:identificador>',views.resetear,name='resetear'),
]