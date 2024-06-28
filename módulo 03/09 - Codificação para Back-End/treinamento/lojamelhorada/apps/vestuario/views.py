
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def Listageral (request):
    busca_abencoados = abencoado.objects.all()
    busca_tacas = taca.objects.all()
    return render(request, "index.html", {"abencoados": busca_abencoados, })

def Criarabencoado(request):
    if request.method == "post":
        novo_abencoado = Formularioabencoado(request.POST)
        if novo_abencoado.is_valid():
            novo_abencoado.save()
            return redirect("pg_inicial")