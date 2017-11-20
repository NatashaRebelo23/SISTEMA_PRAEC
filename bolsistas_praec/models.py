from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Aluno (models.Model):
    matricula = models.CharField(max_length=15,primary_key=True)
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=15)
    curso = models.CharField(max_length=80)
    periodo = models.CharField(max_length=15, null=True)
    renda_familiar = models.CharField(max_length=15)
    data_preenchimento = models.DateField()
    data_preenchimento_termino = models.DateField()
    #nome_Inst = models.CharField(max_length=80)
    #prazo de 23 meses -> 

    def get_absolute_url(self):
        return reverse('bolsistas_praec:aluno_detail', args=[str(self.matricula)]) 

    def __str__(self):
        return self.nome

class Siape(models.Model):
    siape = models.CharField(max_length=9)

    def __str_(self):
        return self.siape

class Usuario (models.Model):
#siape é a matrícula dos servidores
    siape = models.CharField(max_length=20, primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def publish(self):
        self.save()

    def __str__(self):
        return self.siape

        #renda máxima 1405,50 reais
class Bolsa_Auxilio (models.Model):
    aluno = models.OneToOneField(Aluno,on_delete=models.CASCADE)    #chave estrangeira
    tipo_bolsa_auxilio = (
        ('REU','REU'),
        ('ITA','ITA'),
        ('KIT ODONTOLOGICO','KIT ODONTOLOGICO'),
        ('KIT LUPAS MANUAIS','KIT LUPAS MANUAIS')
        )
    tipo = models.CharField(max_length=17,choices=tipo_bolsa_auxilio)

#auxílio creche -> 3 anos e 10 meses - aviso prazo máximo de 3 anos e 11 meses
class Bolsa_Remunerada_400(models.Model):
    aluno = models.OneToOneField(Aluno,on_delete=models.CASCADE)
    tipo_bolsa_remunerada = (
        ('BAE','BAE'),
        ('BIAMA','BIAMA'),
        ('BINCS','BINCS'),
        ('APEC','APEC'),
        ('BIAE','BIAE'),
        ('BIAF','BIAF')
        )
    tipo = models.CharField(max_length=5,choices=tipo_bolsa_remunerada)
    
#emergencial de 3 meses quando o aluno precisa fora do prazo do edital (pode edital de Bae)
#- dependendo da data do edital o aluno reccebe a diferença dos 24 meses da BAE
