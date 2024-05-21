from django.db import models

class aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    idade = models.IntegerField()
    CPF = models.IntegerField()
    telefone = models.IntegerField()
    nomes_dos_pais = models.CharField(max_length=50)
    data_da_matricula = models.DateTimeField()


