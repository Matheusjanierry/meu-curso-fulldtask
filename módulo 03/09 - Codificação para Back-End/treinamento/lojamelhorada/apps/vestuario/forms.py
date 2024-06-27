
from django import forms
from .models import *

class Formularioabencoado(forms.ModelForm):
    class Meta:
        model = abencoado
        fields = ['__all__']

class formulariotaca(forms.ModelForm):
    class meta:
        model = taca 
        fields = ["__all__"]       