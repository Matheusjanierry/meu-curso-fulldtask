from django import forms
from .models import *

class Formulariocadastroe(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ["__all__"]


class Formularioproduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["__all__"]