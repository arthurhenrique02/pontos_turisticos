from django.contrib import admin

from .models import Comentario


# criar model para o site admin
class ComentarioAdmin(admin.ModelAdmin):
    # definir model
    model = Comentario

    # definir fields
    fields = [
        "user",
        "comentario",
        "status",
        "avaliacao",
    ]


# registrar os 2 models
admin.site.register(Comentario, ComentarioAdmin)
