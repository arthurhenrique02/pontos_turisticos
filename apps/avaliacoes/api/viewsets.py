from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from apps.avaliacoes.models import Avaliacao
from .serializers import AvaliacoesSerializer


# criar class viewset
class AvaliacoesViewSet(ModelViewSet):
    # definir queryset
    queryset = Avaliacao.objects.all()

    # definir serializer
    serializer_class = AvaliacoesSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
