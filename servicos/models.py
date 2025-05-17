from django.db import models

class Servicos(models.Model):

    nome = models.CharField(max_length=50)
    duracao = models.TimeField()
    preco = models.IntegerField()

    def __str__(self):
        return self.nome