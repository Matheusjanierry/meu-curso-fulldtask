from django.shortcuts import render
from .models import *



def pagina_inicial(request):
    return render(request, "index.html")


def VerClientes(request):
    clientes_lista = cliente.objects.all()
    return render(request, "lista-clientes.html", {"cliente": clientes_lista})

