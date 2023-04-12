from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from apps.pontos_turisticos.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


# criar view set
class PontoTuristicoViewSet(ModelViewSet):
    # definir query set (provisoriamente o .all)
    queryset = PontoTuristico.objects.all()

    # definir serializer
    serializer_class = PontoTuristicoSerializer

    # adicionar paginação
    pagination_class = LimitOffsetPagination
