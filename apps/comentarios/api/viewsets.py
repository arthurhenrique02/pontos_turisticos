from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ComentariosSerializer
from apps.comentarios.models import Comentario


# criar viewset
class ComentariosViewSet(ModelViewSet):
    # adicionar metodo de autenticação
    authentication_classes = (TokenAuthentication,)

    # adicionar permissão (ser autenticado, ou apenas poder ler as infos)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # definir queryset
    queryset = Comentario.objects.all()

    # definir serializer class
    serializer_class = ComentariosSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
