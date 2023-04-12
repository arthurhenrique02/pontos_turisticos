from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.enderecos.api.viewsets import EnderecosViewSet


# definir router
router = routers.DefaultRouter()
# registrar rota
router.register("", EnderecosViewSet, basename="enderecos")

urlpatterns = [
    # adicionar ao path
    path("", include(router.urls)),
]
