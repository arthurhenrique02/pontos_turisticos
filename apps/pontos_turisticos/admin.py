from django.contrib import admin

from .models import PontoTuristico


# criar model para o site admin
class PontoTuristicoAdmin(admin.ModelAdmin):
    # definir model
    model = PontoTuristico

    # definir fields
    fields = [
        "nome",
        "descricao",
        "status",
    ]


# registrar os 2 models
admin.site.register(PontoTuristico, PontoTuristicoAdmin)
