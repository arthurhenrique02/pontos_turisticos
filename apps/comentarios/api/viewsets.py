from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .serializers import ComentariosSerializer
from apps.comentarios.models import Comentario


# criar viewset
class ComentariosViewSet(ModelViewSet):
    # definir queryset
    queryset = Comentario.objects.all()

    # definir serializer class
    serializer_class = ComentariosSerializer

    # definir pagination
    pagination_class = LimitOffsetPagination
