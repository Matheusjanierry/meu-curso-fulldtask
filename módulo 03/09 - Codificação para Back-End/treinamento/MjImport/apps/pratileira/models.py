from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor_produto = models.DecimalField(max_digits=100,decimal_places=2)
# Create your models here.
    def __str__(self):
        return self.nome_produto
    