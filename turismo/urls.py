from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # incluir rotas de pontos turisticos
    path("pontos-turisticos/", include("apps.pontos_turisticos.urls")),
    # incluir rotas de atrações
    path("atracoes/", include("apps.atracoes.urls")),
    # incluir rotas de atrações
    path("enderecos/", include("apps.enderecos.urls")),
    # incluir rotas de atrações
    path("comentarios/", include("apps.comentarios.urls")),
]
