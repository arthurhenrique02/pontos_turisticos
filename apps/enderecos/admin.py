from django.contrib import admin

from .models import Endereco


# criar model para o site admin
class EnderecoAdmin(admin.ModelAdmin):
    # definir model
    model = Endereco

    # definir fields
    fields = [
        "dados",
        "cidade",
        "estado",
        "pais",
        "latitude",
        "longitude",
    ]


# registrar os 2 models
admin.site.register(Endereco, EnderecoAdmin)
