from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.comentarios.api.viewsets import ComentariosViewSet


# definir router
router = routers.DefaultRouter()
# registrar rota
router.register("", ComentariosViewSet, basename="atracoes")

urlpatterns = [
    # adicionar ao path
    path("", include(router.urls)),
]
