from django.contrib import admin

from .models import PontoTuristico
from .actions import aprova_ponto_turistico, reprova_ponto_turistico


# criar model para o site admin
class PontoTuristicoAdmin(admin.ModelAdmin):
    # definir model
    model = PontoTuristico

    # definir fields
    fields = [
        "nome",
        "endereco",
        "descricao",
        "status",
        "atracoes",
        "avaliacoes",
        "imagem",
    ]

    # adicionar actions
    actions = [aprova_ponto_turistico, reprova_ponto_turistico]

# registrar os 2 models
admin.site.register(PontoTuristico, PontoTuristicoAdmin)
