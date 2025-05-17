from django.db import models
from clientes.models import Clientes
from servicos.models import Servicos
from profissionais.models import Profissionais

class Agendamentos(models.Model):

    cliente = models.ForeignKey(Clientes, related_name="agendamentos", on_delete=models.PROTECT)
    profissional = models.ForeignKey(Profissionais, related_name="agendamentos", on_delete=models.PROTECT)
    servicos = models.ManyToManyField(Servicos, related_name="agendamentos")
    data_agendamento = models.DateTimeField()

    def __str__(self):
        return f"Agendamento de {self.cliente} com {self.profissional} em {self.data_agendamento}"