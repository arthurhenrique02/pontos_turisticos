from rest_framework import serializers

from apps.atracoes.models import Atracao


# criar serializer
class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        # definir model
        model = Atracao

        # definir fields
        fields = [
            "nome",
            "descricao",
            "horario_abertura",
            "horario_fechamento",
            "idade_min",
        ]
