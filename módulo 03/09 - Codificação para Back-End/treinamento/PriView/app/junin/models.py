from django.db import models

tipo_choices = (
        ("M" , "Masculino"),
        ("F" , "Feminino"),
        ("T" , "Transexuais")
    )

Nome = models.CharField(max_length=30)
tipo = models.CharField(max_length=2, choices=tipo_choices)
RG = models.CharField(max_length=20)
CPF = models.IntegerField()
Sexo = models.CharField(max_length=10)
Natural_De = models.CharField(max_length=25)
Estado_Civil = models.CharField(max_length=15)
Identidade = models.IntegerField()
Data_de_Nascimento = models.DateField()
Email = models.EmailField()
CEP = models.IntegerField
Endereço = models.CharField(max_length=35)
Cidade = models.CharField(max_length=20)
Bairro = models.CharField(max_length=20)
UF = models.CharField(max_length=5)
Telefone = models.IntegerField()

preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")


def __str__(self):
    return self
    
        
class PrecoProduto(models.Model):
    Preço_unitario = models.DecimalField(decimal_places=2, max_digits=10, null=True,blank=10)
    Preço_Combinado = models.IntegerField(max_length=20, null=True, blank=True)
    Preço_Atributo = models.IntegerField(null=True,blank=True)
    Total_Unit_e_Comb = models.IntegerField()
    

    class Meta:
            ordering = ('pk',)
            verbose_name =  'Preço Produto'
            verbose_name_plural = 'Preços Produtos'

    
    

