from rest_framework import serializers

from apps.pontos_turisticos.models import PontoTuristico
from apps.enderecos.models import Endereco
from apps.atracoes.models import Atracao
from apps.avaliacoes.models import Avaliacao


# criar serializer
class PontoTuristicoSerializer(serializers.ModelSerializer):
    # definir slug para mostrar determinados nomes
    # endereço
    endereco = serializers.SlugRelatedField(
        queryset=Endereco.objects.all(), slug_field="dados"
    )
    # many=True é para fields m2m
    # atraçoes (mostrar o nome)
    atracoes = serializers.SlugRelatedField(
        many=True, queryset=Atracao.objects.all(), slug_field="nome"
    )
    # mostrar as estrelas das avaliacoes
    avaliacoes = serializers.SlugRelatedField(
        many=True, queryset=Avaliacao.objects.all(), slug_field="estrelas"
    )

    # criar meta
    class Meta:
        # definir model
        model = PontoTuristico

        # definir fields
        fields = [
            "id",
            "endereco",
            "nome",
            "descricao",
            "status",
            "atracoes",
            "comentarios",
            "avaliacoes",
        ]
