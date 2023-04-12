from rest_framework import serializers

from django.contrib.auth.models import User
from apps.avaliacoes.models import Avaliacao


# criar serializer
class AvaliacoesSerializer(serializers.ModelSerializer):
    # pegar username do usuario
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )

    class Meta:
        # definir model
        model = Avaliacao

        # definir fields
        fields = [
            "user",
            "estrelas",
        ]
