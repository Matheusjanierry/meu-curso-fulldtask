from django.db import models

class estudante(models.Model):
    nome = models.CharField(max_length=50)

    tipo_sexo = (
        ("M" "Masculino")
        ("F" "Feminino") 
              )
    def __str__(self):
        return self.nome
    
    sexo = models.CharField(max_length=2, choices=tipo_sexo)
    valor = models.DecimalField(max_length=4, decimal_places=2)
    preco = models.DecimalField(max_length=10, decimal_places=2, verbose_name="preço")

class PrecoProdutos(models.Model):
    class Meta:
        ordering = ('pk',)
        verbose_name = 'Preço Produto'
        verbose_name_plural = 'Preços Produtos'
        foto = models.ImageField(upload_to="foto_perfil/")
