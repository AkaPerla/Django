from django.urls import path
from .views import RecetarioListView

urlpatterns = [
    path('',RecetarioListView.as_view(), name='recetas')
]
