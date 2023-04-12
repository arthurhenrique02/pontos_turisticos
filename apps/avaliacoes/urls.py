from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.avaliacoes.api.viewsets import AvaliacoesViewSet


# definir router
router = routers.DefaultRouter()
# registrar rota
router.register("", AvaliacoesViewSet, basename="avaliacoes")

urlpatterns = [
    # adicionar ao path
    path("", include(router.urls)),
]
