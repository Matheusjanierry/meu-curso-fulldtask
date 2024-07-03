from django.shortcuts import render
from. models import *
from .models import *

def verindex(request):
    buscar_produtos = Produto.objects.all()
    return render(request, 'produto.html', {'produto': buscar_produtos})
