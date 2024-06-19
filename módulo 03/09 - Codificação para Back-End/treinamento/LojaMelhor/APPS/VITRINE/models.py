from django.db import models

class produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor_produto = models.DecimalField(max_digits=1000)