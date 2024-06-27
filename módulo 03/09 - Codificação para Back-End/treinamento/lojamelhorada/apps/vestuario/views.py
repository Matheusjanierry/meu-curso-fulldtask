
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def criarpessoa(request):
    busca_abencoado = abencoado.objects.all()
    return render(request, "abencoado.html", {"abencoados": busca_abencoado})
    