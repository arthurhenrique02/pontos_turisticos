from rest_framework import serializers

from apps.enderecos.models import Endereco


# criar serializer
class EnderecoSerializer(serializers.ModelSerializer):
    # criar Meta
    class Meta:
        # definir model
        model = Endereco

        # definir fiels
        fields = [
            "dados",
            "cidade",
            "estado",
            "pais",
        ]
