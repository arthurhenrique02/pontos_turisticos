from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .serializers import EnderecosSerializer
from apps.enderecos.models import Endereco


# criar viewset
class EnderecosViewSet(ModelViewSet):
    # definir queryset
    queryset = Endereco.objects.all()

    # definir serializer class
    serializer_class = EnderecosSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
