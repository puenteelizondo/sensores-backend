from django.db import models
from django.utils import timezone

class Temperatura(models.Model):
    valor = models.FloatField(help_text="Temperatura en grados Celsius")
    fecha_hora = models.DateTimeField(default=timezone.now)
    sensor_id = models.CharField(max_length=50, default="TEMP_01")
    
    class Meta:
        db_table = 'temperatura'
        ordering = ['-fecha_hora']
        verbose_name = 'Temperatura'
        verbose_name_plural = 'Temperaturas'
    
    def __str__(self):
        return f"Temp: {self.valor}°C - {self.fecha_hora}"

class Humedad(models.Model):
    valor = models.FloatField(help_text="Humedad en porcentaje")
    fecha_hora = models.DateTimeField(default=timezone.now)
    sensor_id = models.CharField(max_length=50, default="HUM_01")
    
    class Meta:
        db_table = 'humedad'
        ordering = ['-fecha_hora']
        verbose_name = 'Humedad'
        verbose_name_plural = 'Humedades'
    
    def __str__(self):
        return f"Humedad: {self.valor}% - {self.fecha_hora}"

class Distancia(models.Model):
    valor = models.FloatField(help_text="Distancia en centímetros")
    fecha_hora = models.DateTimeField(default=timezone.now)
    sensor_id = models.CharField(max_length=50, default="DIST_01")
    
    class Meta:
        db_table = 'distancia'
        ordering = ['-fecha_hora']
        verbose_name = 'Distancia'
        verbose_name_plural = 'Distancias'
    
    def __str__(self):
        return f"Distancia: {self.valor}cm - {self.fecha_hora}"