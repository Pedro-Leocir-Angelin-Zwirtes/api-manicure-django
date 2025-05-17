from rest_framework import serializers
from agendamentos import models
from clientes.models import Clientes
from profissionais.models import Profissionais
from servicos.models import Servicos
from django.utils import timezone
from django.utils.timezone import make_aware

DIAS_SEMANA = {
    0: "Segunda",
    1: "Terça",
    2: "Quarta",
    3: "Quinta",
    4: "Sexta",
    5: "Sabado",
    6: "Domingo",
}

class AgendamentosSerializers(serializers.ModelSerializer):

    nome_cliente = serializers.SerializerMethodField()
    nome_profissional = serializers.SerializerMethodField()
    nomes_servicos = serializers.SerializerMethodField()

    class Meta:
        model = models.Agendamentos
        fields = [
            'id',
            'cliente',
            'nome_cliente',
            'profissional',
            'nome_profissional',
            'servicos',
            'nomes_servicos',
            'data_agendamento'
        ]
    
    def get_nome_cliente(self, obj):
        return obj.cliente.nome if obj.cliente else None
    
    def get_nome_profissional(self, obj):
        return obj.profissional.nome if obj.profissional else None
    
    def get_nomes_servicos(self, obj):
        return [servico.nome for servico in obj.servicos.all()]
    
    #Verificando dia de agendamento com dia disponivel do profissional
    def validate(self, data):
        profissional = data.get('profissional')
        cliente = data.get('cliente')
        data_agendamento = data.get('data_agendamento')
        servicos = data.get('servicos', [])

        if data_agendamento < timezone.now():
            raise serializers.ValidationError("A data da consulta não pode ser anterior a data atual")

        if profissional and data_agendamento:
            dia_semana = data_agendamento.weekday()
            nome_dia = DIAS_SEMANA[dia_semana]

            if not profissional.dias_trabalho.filter(nome=nome_dia).exists():
                raise serializers.ValidationError({
                'data_agendamento': f"{profissional.nome} não trabalha no dia {nome_dia}."
            })

        if models.Agendamentos.objects.filter(cliente=cliente, data_agendamento=data_agendamento).exists():
            raise serializers.ValidationError({
                'cliente': f"{cliente.nome} já tem um agendamento nesse horário."
            })

        if models.Agendamentos.objects.filter(profissional=profissional, data_agendamento=data_agendamento).exists():
            raise serializers.ValidationError({
                'profissional': f"{profissional.nome} já tem um agendamento nesse horário."
            })

        if profissional and servicos:
            servicos_profissional_ids = profissional.especialidade.values_list('id', flat=True)
            for servico in servicos:
                if servico.id not in servicos_profissional_ids:
                    raise serializers.ValidationError({
                        "servicos": f"O serviço '{servico.nome}' não é oferecido por {profissional.nome}."
                    })

        return data