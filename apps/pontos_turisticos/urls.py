from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.pontos_turisticos.api.viewsets import PontoTuristicoViewSet

# definir router
router = routers.DefaultRouter()
# registrar rota
router.register("", PontoTuristicoViewSet, basename="pontoTuristico")

urlpatterns = [
    # adicionar ao path
    path("", include(router.urls)),
]
