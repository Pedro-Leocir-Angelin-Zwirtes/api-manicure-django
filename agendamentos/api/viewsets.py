from rest_framework import viewsets,filters
from agendamentos.api import serializers
from agendamentos import models

class AgendamentosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.AgendamentosSerializers
    queryset = models.Agendamentos.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente__nome', 'profissional__nome', 'servicos__nome', 'data_agendamento']