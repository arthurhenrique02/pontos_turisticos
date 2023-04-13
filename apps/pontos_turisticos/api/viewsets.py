from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

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

    # sobrescrever get_queryset
    def get_queryset(self):
        # query set padrao = pegar todos os objetos
        queryset = PontoTuristico.objects.all()

        # queryset para um determinado status
        # transformar em string e escrever com primeira letra maiuscula (capitalize)
        status = self.request.query_params.get("status")

        # mudar queryset
        if status:
            queryset = PontoTuristico.objects.filter(status=status)

        # retornar query
        return queryset

    # sobrescrever List (GET all)
    def list(self, request, *args, **kwargs):
        # retornar apenas os pontos turisticos aprovados (status=True)
        queryset = PontoTuristico.objects.filter(status=True)
        return Response(PontoTuristicoSerializer(queryset, many=True).data)