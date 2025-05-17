from django.db import models

class Clientes(models.Model):

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome