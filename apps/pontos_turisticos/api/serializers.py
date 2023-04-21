from rest_framework import serializers

from apps.pontos_turisticos.models import PontoTuristico
from apps.enderecos.models import Endereco
from apps.atracoes.models import Atracao
from apps.avaliacoes.models import Avaliacao

from apps.avaliacoes.api.serializers import AvaliacoesSerializer
from apps.enderecos.api.serializers import EnderecosSerializer


# criar serializer
class PontoTuristicoSerializer(serializers.ModelSerializer):
    # criar nested relation para endereço
    endereco = EnderecosSerializer()

    # many=True é para fields m2m
    # atraçoes (mostrar o nome)
    atracoes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="nome"
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

    # criar função para criar avaliacoes
    def cria_avaliacao(self, avaliacoes, ponto_turistico):
        # iterar lista de avaliacoes
        for avaliacao in avaliacoes:
            # criar a avaliacao
            avaliacao_criada = Avaliacao.objects.create(**avaliacao)

            # adicionar avaliacao ao ponto turistico
            ponto_turistico.avaliacoes.add(avaliacao_criada)


    # sobrescrever o create
    def create(self, validated_data):
        # pegar as avaliacoes da request
        avalicoes = validated_data["avaliacoes"]

        # remover as avaliacoes da request
        del validated_data["avaliacoes"]

        # pegar endereco digitado
        endereco = validated_data["endereco"]
        # remover da request
        del validated_data["endereco"]

        # criar o ponto turistico, passar o dicionario desempacotado e o endereço
        ponto_turistico = PontoTuristico.objects.create(**validated_data, endereco=Endereco.objects.create(**endereco))

        #criar avaliacao para o ponto turistico
        self.cria_avaliacao(avalicoes, ponto_turistico)

        # retornar ponto turistico
        return ponto_turistico
    
    # definir a função de get para o serializer method field
    def get_descricao_completa(self, obj):
        return f"{obj.nome} - {obj.descricao}"
