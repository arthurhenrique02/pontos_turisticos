from django.contrib import admin

from .models import Comentario
from .actions import aprova_comentario, reprova_comentario

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
    # adicionar actions
    actions = [aprova_comentario, reprova_comentario]


# registrar os 2 models
admin.site.register(Comentario, ComentarioAdmin)
