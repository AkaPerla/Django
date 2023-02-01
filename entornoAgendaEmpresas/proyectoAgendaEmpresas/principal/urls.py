from django.urls import path
# from . import views
from .views import EmpresaListView,EmpresaDetailView

urlpatterns = [
    path('',EmpresaListView.as_view(), name='listado'),
    path('empresa/<int:pk>',EmpresaDetailView.as_view(), name='detalles'),
]