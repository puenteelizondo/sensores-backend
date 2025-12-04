from rest_framework import serializers
from .models import Temperatura, Humedad, Distancia

class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = ['id', 'valor', 'fecha_hora', 'sensor_id']
        read_only_fields = ['id', 'fecha_hora']

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = ['id', 'valor', 'fecha_hora', 'sensor_id']
        read_only_fields = ['id', 'fecha_hora']

class DistanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distancia
        fields = ['id', 'valor', 'fecha_hora', 'sensor_id']
        read_only_fields = ['id', 'fecha_hora']