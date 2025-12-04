from django.contrib import admin
from .models import Temperatura, Humedad, Distancia

@admin.register(Temperatura)
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'valor', 'sensor_id', 'fecha_hora']
    list_filter = ['sensor_id', 'fecha_hora']
    search_fields = ['sensor_id']
    ordering = ['-fecha_hora']

@admin.register(Humedad)
class HumedadAdmin(admin.ModelAdmin):
    list_display = ['id', 'valor', 'sensor_id', 'fecha_hora']
    list_filter = ['sensor_id', 'fecha_hora']
    search_fields = ['sensor_id']
    ordering = ['-fecha_hora']

@admin.register(Distancia)
class DistanciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'valor', 'sensor_id', 'fecha_hora']
    list_filter = ['sensor_id', 'fecha_hora']
    search_fields = ['sensor_id']
    ordering = ['-fecha_hora']