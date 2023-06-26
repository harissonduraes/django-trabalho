from django.db import models

# Create your models here.



class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=50)
    periodo = models.CharField('Período', max_length=100)
    nota = models.IntegerField('Nota', max_length=3)
    situacao = models.BooleanField('Situação')
    def __str__(self) -> str:
        return self.nome