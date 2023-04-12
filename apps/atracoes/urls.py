from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.atracoes.api.viewsets import AtracoesViewSet


# definir router
router = routers.DefaultRouter()
# registrar rota
router.register("", AtracoesViewSet, basename="atracoes")

urlpatterns = [
    # adicionar ao path
    path("", include(router.urls)),
]
