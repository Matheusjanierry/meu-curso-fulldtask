from django.shortcuts import render
from.models import *

def pagina_inicial(request):
    return render(request, "index.html")

def paginapacientes(request):
    busca = Paciente.objects.all()
    return render(request, "lista-pacientes.html", {"pacientes":busca})

def paginadoutores(request):
    busca = Doutor.objects.all
    return render(request, "lista-doutores.html", {"doutores": busca})
