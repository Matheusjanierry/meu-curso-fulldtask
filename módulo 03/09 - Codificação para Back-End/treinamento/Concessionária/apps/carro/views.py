from django.shortcuts import render
from. models import *
# Create your views here.

def linkInicial(request):
    return render(request, 'index.html')
def linkCadastro(request):
    lista_cadastro = Cadastro.objects.all()
    return render(request, 'cadastro.html', {'cadastro': lista_cadastro })
def linkCliente(request):
    lista_cliente = cliente.objects.all()
    return render(request, 'cliente.html', {'cadastro': lista_cliente})
def linkVendedor(request):
    lista_vendedor = vendedor.objects.all()
    return render(request, 'cadastro.html', {'cadastro': lista_vendedor})
def linkProduto(request):
    lista_produto = Produto.objects.all()
    return render(request, 'cadastro.html', {'cadastro': lista_produto})