from django.db import models

# Create your models here.
class abencoado(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self. nome
class taca(models.Model):
    dono = models.ForeignKey(abencoado, on_delete= models)
    motivo = models.CharField()
    instrumento = models.CharField()

    def __str__(self):
        return self. dono.nome + " | taca"
    
