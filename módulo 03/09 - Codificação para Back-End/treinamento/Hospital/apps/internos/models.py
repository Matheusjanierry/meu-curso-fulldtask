from django.db import models
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    diagnostico = models.TextField()

    def __str__(self):
        return self.nome
    

class Doutor(models.Model):
        nome = models.CharField(max_length=50)
        especializacao = models.CharField(max_length=50)
        crm = models.PositiveBigIntegerField()

        
        def __str__(self):
            return self.nome
    
        class meta:
            verbose_name = "Doutor"
            verbose_name_plural = "Doutores"

class Resultado(models.Model):
        infermidade = models.CharField(max_length=50)
        tipo = models.CharField(max_length=50)
        gravidade = models.PositiveBigIntegerField()

        def __str__(self):
            return self.infermidade
        
class Procedimentos(models.Model):
        repouso = models.CharField(max_length=50)
        tempo = models.CharField(max_length=15)
        medicamento = models.PositiveBigIntegerField()
        forma_de_aplicar = models.CharField(max_length=40)
        

        def __str__(self):
            return self.repouso

