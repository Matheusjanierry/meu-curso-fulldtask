from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor_produto = models.DecimalField(decimal_places=2,max_digits=6)
    foto_produto = models.ImageField(upload_to="foto_principal/")
    def __str__(self):
        return self.nome_produto
    
class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.nome
    
class vendedor(models.Model):
    nome_vendedor = models.CharField(max_length=100)
    matricula = models.IntegerField()
    email = models.EmailField()
    contato = models.IntegerField()
    def __str__(self):
        return self.nome_vendedor
    
class cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    cpf = models.IntegerField()
    email = models.EmailField()
    contato = models.IntegerField()
    def __str__(self):
        return self.nome_cliente
    
    