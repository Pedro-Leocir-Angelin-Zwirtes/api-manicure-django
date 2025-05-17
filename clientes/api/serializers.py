from rest_framework import serializers
from clientes import models

class ClientesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Clientes
        fields = '__all__'