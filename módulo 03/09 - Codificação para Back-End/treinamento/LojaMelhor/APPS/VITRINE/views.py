from django.shortcuts import render
from .models import *

def VerProdutos(request):
    produtos_lista = produto.objects.all()
    return render(request, "lista-produtos.html", {"produtos": produtos_lista})

def DetalhesProduto(request, id_produto):
    busca = produto.objects.get(id=id_produto)
    return render(request, "detalhes_produto.html", {"produto": busca})
