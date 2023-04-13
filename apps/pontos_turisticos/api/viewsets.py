from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from apps.pontos_turisticos.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


# criar view set
class PontosTuristicosViewSet(ModelViewSet):
    # definir query set (provisoriamente o .all)
    # queryset = PontoTuristico.objects.all()

    # definir serializer
    serializer_class = PontoTuristicoSerializer

    # adicionar paginação
    pagination_class = LimitOffsetPagination

    # sobreescrever get_queryset
    def get_queryset(self):
        # query set padrao = pegar todos os objetos
        queryset = PontoTuristico.objects.all()

        # queryset para um determinado status
        # transformar em string e escrever com primeira letra maiuscula (capitalize)
        status = self.request.query_params.get("status")

        # tratar queryset
        # if status.is):
        #     status = "True"

        # mudar queryset
        if status:
            queryset = PontoTuristico.objects.filter(status=status)

        # retornar query
        return queryset
