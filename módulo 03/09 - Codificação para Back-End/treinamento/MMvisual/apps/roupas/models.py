from django.db import models

class clientes(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    CPF= models.IntegerField()

    def __str__(self):
        return self.nome
    
class produtos(models.Model):
        nome_do_produto = models.CharField(max_length=50)
        marcar_do_produto= models.CharField(max_length=50)
        descricao= models.TextField()
        valor_do_produto=models.FloatField()

        