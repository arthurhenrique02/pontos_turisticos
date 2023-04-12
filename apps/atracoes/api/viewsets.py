from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from apps.atracoes.models import Atracao
from .serializers import AtracaoSerializer


# criar class viewset
class AtracoesViewSet(ModelViewSet):
    # definir queryset
    queryset = Atracao.objects.all()

    # definir serializer
    serializer_class = AtracaoSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
