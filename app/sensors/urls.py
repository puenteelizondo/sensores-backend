from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TemperaturaViewSet,
    HumedadViewSet,
    DistanciaViewSet,
    ReporteViewSet,
    SensoresUltimosViewSet,
    LedViewSet
)

router = DefaultRouter()
router.register(r'temperatura', TemperaturaViewSet, basename='temperatura')
router.register(r'humedad', HumedadViewSet, basename='humedad')
router.register(r'distancia', DistanciaViewSet, basename='distancia')
router.register(r'reporte', ReporteViewSet, basename='reporte')
router.register(r'sensores', SensoresUltimosViewSet, basename='sensores')
router.register(r'led', LedViewSet, basename='led')


urlpatterns = [
    path('', include(router.urls)),
]
