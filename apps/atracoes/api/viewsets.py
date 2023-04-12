from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from apps.atracoes.models import Atracao
from .serializers import AtracoesSerializer


# criar class viewset
class AtracoesViewSet(ModelViewSet):
    # definir queryset
    queryset = Atracao.objects.all()

    # definir serializer
    serializer_class = AtracoesSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
