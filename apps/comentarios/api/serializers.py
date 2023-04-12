from rest_framework import serializers

from django.contrib.auth.models import User
from apps.comentarios.models import Comentario
from apps.avaliacoes.models import Avaliacao


# criar serializer
class ComentariosSerializer(serializers.ModelSerializer):
    # pegar username do usuario
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )
    # pegar nota da avaliacao
    avaliacao = serializers.SlugRelatedField(
        queryset=Avaliacao.objects.all(),
        slug_field="estrelas",
    )

    # criar Meta
    class Meta:
        # definir model
        model = Comentario

        # definir fields
        fields = [
            "user",
            "comentario",
            "data",
            "status",
            "avaliacao",
        ]
