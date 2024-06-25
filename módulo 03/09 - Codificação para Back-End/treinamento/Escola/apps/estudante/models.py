from django.db import models


class Estudante(models.Model):
    nome_aluno = models.CharField(max_length=100)
    nota_final = models.IntegerField()

    def __str__(self):
        return self.nome_aluno
    
