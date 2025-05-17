from rest_framework import serializers
from profissionais import models

class ProfissionaisSerializers(serializers.ModelSerializer):
    nome_especialidade = serializers.SerializerMethodField()
    dias_trabalho_nomes = serializers.SerializerMethodField()

    class Meta:
        model = models.Profissionais
        fields = [
            'id',
            'nome',
            'especialidade',
            'nome_especialidade',
            'dias_trabalho',
            'dias_trabalho_nomes',
            'hora_inicio_trabalho',
            'hora_final_trabalho'
        ]

    def get_nome_especialidade(self, obj):
        return [especialidade.nome for especialidade in obj.especialidade.all()]
    
    def get_dias_trabalho_nomes(self, obj):
        return [dia.nome for dia in obj.dias_trabalho.all()]
    
    def validate(self, data):
        hora_comeco = data.get('hora_inicio_trabalho')
        hora_final = data.get('hora_final_trabalho')

        if hora_final <= hora_comeco:
            raise serializers.ValidationError("A hora final não pode ser anterior ou igual a hora inicial")

        return data