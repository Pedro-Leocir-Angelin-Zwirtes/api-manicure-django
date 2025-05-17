from rest_framework import serializers
from servicos import models

class ServicosSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Servicos
        fields = '__all__'

