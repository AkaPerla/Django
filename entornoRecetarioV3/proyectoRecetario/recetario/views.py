from django.views.generic.list import ListView
from .models import Receta

# Create your views here.
class RecetarioListView(ListView):
    model = Receta
