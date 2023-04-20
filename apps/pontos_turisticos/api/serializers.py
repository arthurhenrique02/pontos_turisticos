from rest_framework import serializers

from apps.pontos_turisticos.models import PontoTuristico
from apps.enderecos.models import Endereco
from apps.atracoes.models import Atracao
from apps.avaliacoes.models import Avaliacao
from apps.avaliacoes.api.serializers import AvaliacoesSerializer


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
    # utilizando nested relationship para exibir as avaliacoes
    # pode-se criar um outro serializer e definir os fields, ou utilizar o mesmo
    # Cria-se outro caso desejo um mais completo, ou um mais simples que o padrao
    avaliacoes = AvaliacoesSerializer(many=True)

    # adicionando serializer method field
    descricao_completa = serializers.SerializerMethodField()

    # criar meta
    class Meta:
        # definir model
        model = PontoTuristico

        # definir fields
        fields = [
            "id",
            "nome",
            "endereco",
            "descricao",
            "status",
            "imagem",
            "atracoes",
            "comentarios",
            "avaliacoes",
            "descricao_completa",
            "descricao_completa_no_model",
        ]

    # definir a função de get para o serializer method field
    def get_descricao_completa(self, obj):
        return f"{obj.nome} - {obj.descricao}"
