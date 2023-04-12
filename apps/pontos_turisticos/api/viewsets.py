from rest_framework.viewsets import ModelViewSet

from apps.pontos_turisticos.models import PontoTuristico

from .serializers import PontoTuristicoSerializer

# criar view set
class PontoTuristicoViewSet(ModelViewSet):

    # definir query set (provisoriamente o .all)
    queryset = PontoTuristico.objects.all()

    # definir serializer
    serializer_class = PontoTuristicoSerializer