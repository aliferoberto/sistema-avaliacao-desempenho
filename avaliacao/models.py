from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Colaborador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Criterio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    peso = models.IntegerField(default=1)

    def __str__(self):
        return self.nome
    
class Avaliacao(models.Model):
    avaliador = models.ForeignKey(
        Colaborador, on_delete=models.CASCADE,
        related_name='avaliacoes_realizadas'
    )
    avaliado = models.ForeignKey(
        Colaborador, on_delete=models.CASCADE,
        related_name='avaliacoes_recebidas'
    )
    data = models.DateField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.avaliado} - Nota {self.nota}"
    
class Nota(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.criterio}: {self.valor}"

