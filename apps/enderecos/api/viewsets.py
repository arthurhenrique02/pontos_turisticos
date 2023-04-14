from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import EnderecosSerializer
from apps.enderecos.models import Endereco


# criar viewset
class EnderecosViewSet(ModelViewSet):
    # adicionar metodo de autenticação
    authentication_classes = (TokenAuthentication,)

    # adicionar permissão (ser autenticado, ou apenas poder ler as infos)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # definir queryset
    queryset = Endereco.objects.all()

    # definir serializer class
    serializer_class = EnderecosSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
