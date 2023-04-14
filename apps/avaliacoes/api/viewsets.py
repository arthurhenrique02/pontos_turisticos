from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.avaliacoes.models import Avaliacao
from .serializers import AvaliacoesSerializer


# criar class viewset
class AvaliacoesViewSet(ModelViewSet):
    # adicionar metodo de autenticação
    authentication_classes = (TokenAuthentication,)

    # adicionar permissão (ser autenticado, ou apenas poder ler as infos)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # definir queryset
    queryset = Avaliacao.objects.all()

    # definir serializer
    serializer_class = AvaliacoesSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
