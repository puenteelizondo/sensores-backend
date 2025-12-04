from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemperaturaViewSet, HumedadViewSet, DistanciaViewSet, ReporteViewSet

router = DefaultRouter()
router.register(r'temperatura', TemperaturaViewSet, basename='temperatura')
router.register(r'humedad', HumedadViewSet, basename='humedad')
router.register(r'distancia', DistanciaViewSet, basename='distancia')
router.register(r'reporte', ReporteViewSet, basename='reporte')  # ← NUEVO

urlpatterns = [
    path('', include(router.urls)),
]