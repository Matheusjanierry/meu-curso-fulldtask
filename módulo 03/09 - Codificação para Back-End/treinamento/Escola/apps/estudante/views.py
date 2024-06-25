from django.shortcuts import render
from .models import *
from .forms import *


def CriarEstudante(request):
    busca_estudantes = Estudante.objects.all()
    if request.method == "POST":
        novo_estudante = FormularioEstudante(request.POST)
        novo_estudante.save()
        novo_estudante = FormularioEstudante()
    else:
        novo_estudante = FormularioEstudante()
    return render(request, "pagina-estudantes.html", 
                  {"formulario": novo_estudante,
                    "estudantes": busca_estudantes
                    })