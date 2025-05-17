from rest_framework import viewsets, filters
from servicos.api import serializers
from servicos import models

class ServicosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ServicosSerializers
    queryset = models.Servicos.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']