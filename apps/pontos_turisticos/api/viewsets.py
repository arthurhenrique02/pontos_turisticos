from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from apps.pontos_turisticos.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


# criar view set
class PontosTuristicosViewSet(ModelViewSet):
    # adicionar metodo de autenticação
    authentication_classes = (TokenAuthentication,)

    # adicionar permissão (ser autenticado, ou apenas poder ler as infos)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # definir query set (provisoriamente o .all)
    queryset = PontoTuristico.objects.all()

    # definir serializer
    serializer_class = PontoTuristicoSerializer

    # adicionar paginação
    pagination_class = LimitOffsetPagination

    # habilitar filter fields, filtragem é melhor feita utilizando o filterset_fields
    filterset_fields = ["id", "nome", "status"]

    # adicionar filtro search
    filter_backends = (filters.SearchFilter,)

    # adicionar fields que serão filtrados
    search_fields = ["nome", "endereco__dados"]

    # sobrescrever get_queryset
    # def get_queryset(self):
    #     # query set padrao = pegar todos os objetos
    #     queryset = PontoTuristico.objects.all()

    #     # queryset para um determinado id, status
    #     # definir None, caso o usuario não passe nenhum parametro
    #     id = self.request.query_params.get("id", None)
    #     nome = self.request.query_params.get("nome", None)
    #     status = self.request.query_params.get("status", None)

    #     # mudar queryset
    #     # por id
    #     if id:
    #         queryset = queryset.filter(id=id)

    #     # por nome. Ignorar caso sensitivo (__iexact)
    #     if nome:
    #         queryset = queryset.filter(nome__iexact=nome)

    #     # por status
    #     if status:
    #         queryset = queryset.filter(status=status)

    #     # retornar query
    #     return queryset

    # sobrescrever List (GET all)
    # def list(self, request, *args, **kwargs):
    #     # retornar apenas os pontos turisticos aprovados (status=True)
    #     queryset = PontoTuristico.objects.filter(status=True)
    #     return Response(PontoTuristicoSerializer(queryset, many=True).data)

    # para sobrescrever o create (POST)
    # linha não alterada, apenas mostrado em comentario
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # sobrescrever destroy (DELETE)
    # geralmente, é uma necessidade reescrever este metodo
    # def destroy(self, request, *args, **kwargs):
    #     pode-se fazer um soft delete (apenas mudar a flag, por exemplho: mudar de flag=ativa para flag=deleteda)
    #     para evitar deletar do banco de dados (má pratica)
    #     return super().destroy(request, *args, **kwargs)

    # sobrescrever retrive (GET only)
    # def retrieve(self, request, *args, **kwargs):
    #     pode-se adicionar logs para verificar quem acessa
    #     verificar status do usuario, etc
    #     return super().retrieve(request, *args, **kwargs)

    # sobrescrever update (PUT)
    # def update(self, request, *args, **kwargs):
    #     pode-se adicionar as informações anteriores a outra tabela, por exemplo
    #     ...
    #     return super().update(request, *args, **kwargs)

    # sobrescrever o partial_update (PATCH)
    # def partial_update(self, request, *args, **kwargs):
    #    pode-se adicionar as informações anteriores a outra tabela, por exemplo
    #    return super().partial_update(request, *args, **kwargs)

    # criar action de denunciar (basta definir um metodo normalmente e adicionar um decorador @actions())
    # detail que dizer se a action será referente à um recurso, ou a endpoint. Se detail=True, é referente à um recurso
    # @action(methods=["GET"], detail=True) # passar métodos que deseja como parâmetro
    # def denunciar(self, request, pk=None): # pegar request e pk
    #     pass
