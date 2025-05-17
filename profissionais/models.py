from django.db import models
from servicos.models import Servicos
import datetime

class DiasTrabalho(models.Model):

    DIAS_TRABALHO = [
        ("Segunda", "Segunda"),
        ("Terça", "Terça"),
        ("Quarta", "Quarta"),
        ("Quinta", "Quinta"),
        ("Sexta", "Sexta"),
        ("Sabado", "Sabado"),
        ("Domingo", "Domingo"),
    ]

    nome = models.CharField(max_length=10, choices=DIAS_TRABALHO, unique=True)

    def __str__(self):
        return self.nome

class Profissionais(models.Model):

    nome = models.CharField(max_length=255)
    especialidade = models.ManyToManyField(Servicos, related_name="profissionais")
    dias_trabalho = models.ManyToManyField(DiasTrabalho, related_name="profissionais")
    hora_inicio_trabalho = models.TimeField(default='08:00')
    hora_final_trabalho = models.TimeField(default='18:00')

    def __str__(self):
        return self.nome