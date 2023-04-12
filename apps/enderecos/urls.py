from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.enderecos.api.viewsets import EnderecoViewSet


# definir router
router = routers.DefaultRouter()
# registrar rota
router.register("", EnderecoViewSet, basename="enderecos")

urlpatterns = [
    # adicionar ao path
    path("", include(router.urls)),
]
