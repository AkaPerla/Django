from django.urls import path
# from . import views
from .views import EmpresaListView,EmpresaDetailView, EmpresaCreateView, EmpresaDeleteView,EmpresaUpdateView

urlpatterns = [
    path('',EmpresaListView.as_view(), name='listado'),
    path('empresa/<int:pk>',EmpresaDetailView.as_view(), name='detalles'),
    path('crearEmpresa',EmpresaCreateView.as_view(),name='crear'),
    path('borrarEmpresa/<int:pk>',EmpresaDeleteView.as_view(),name='borrar'),
    path('modificarEmpresa/<int:pk>',EmpresaUpdateView.as_view(),name='modificar'),
]