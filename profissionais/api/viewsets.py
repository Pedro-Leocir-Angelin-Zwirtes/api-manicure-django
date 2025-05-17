from rest_framework import viewsets, filters
from profissionais.api import serializers
from profissionais import models
from django_filters.rest_framework import DjangoFilterBackend

class ProfissionaisViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ProfissionaisSerializers
    queryset = models.Profissionais.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome','especialidade__nome', 'dias_trabalho__nome']