from django.contrib import admin

from .models import Atracao


# criar model para o site admin
class AtracaoAdmin(admin.ModelAdmin):
    # definir model
    model = Atracao

    # definir fields
    fields = [
        "nome",
        "descricao",
        "horario_abertura",
        "horario_fechamento",
        "idade_min",
    ]


# registrar os 2 models
admin.site.register(Atracao, AtracaoAdmin)
