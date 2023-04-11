from django.contrib import admin

from .models import Avaliacao


# criar model para o site admin
class AvaliacaoAdmin(admin.ModelAdmin):
    # definir model
    model = Avaliacao

    # definir fields
    fields = [
        "user",
        "estrelas",
    ]


# registrar os 2 models
admin.site.register(Avaliacao, AvaliacaoAdmin)
