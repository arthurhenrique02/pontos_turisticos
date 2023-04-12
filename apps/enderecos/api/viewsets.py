from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .serializers import EnderecoSerializer
from apps.enderecos.models import Endereco


# criar viewset
class EnderecoViewSet(ModelViewSet):
    # definir queryset
    queryset = Endereco.objects.all()

    # definir serializer class
    serializer_class = EnderecoSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
