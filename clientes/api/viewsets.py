from rest_framework import viewsets, filters
from clientes import models
from clientes.api import serializers

class ClientesViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializers
    queryset = models.Clientes.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'telefone']