from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.pontos_turisticos.api.viewsets import PontoTuristicoViewSet

# definir router
router = routers.DefaultRouter()

router.register("", PontoTuristicoViewSet, basename="pontoTuristico")

urlpatterns = [
    path("", include(router.urls)),
]
