from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters

from apps.atracoes.models import Atracao
from .serializers import AtracoesSerializer


# criar class viewset
class AtracoesViewSet(ModelViewSet):
    # adicionar metodo de autenticação
    authentication_classes = (TokenAuthentication,)

    # adicionar permissão (ser autenticado, ou apenas poder ler as infos)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # definir queryset
    queryset = Atracao.objects.all()

    # definir serializer
    serializer_class = AtracoesSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination

    # habilitar filter fields
    filterset_fields = ["id", "nome"]

    # adicionar filtro search
    filter_backends = (filters.SearchFilter,)

    # adicionar fields que serão filtrados
    search_fields = ["nome", "endereco__dados"]
