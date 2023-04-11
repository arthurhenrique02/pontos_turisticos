from django.db import models

from apps.atracoes.models import Atracao
from apps.comentarios.models import Comentario
from apps.avaliacoes.models import Avaliacao
from apps.enderecos.models import Endereco


# criar model de ponto turistico
class PontoTuristico(models.Model):
    # nome
    nome = models.CharField(max_length=100, help_text="nome do ponto turistico")
    # descrição
    descricao = models.CharField(max_length=250, help_text="descrição breve do local")
    # status do local (para verificar se vai para a listagem ou não)
    # setar default=False
    status = models.BooleanField(default=False, help_text="Aprovado/reprovado")

    # relacionar com atração
    atracoes = models.ManyToManyField(Atracao, blank=True)

    # relacionar com comentarios
    comentarios = models.ManyToManyField(Comentario, blank=True)

    # relacionar com avaliações
    avaliacoes = models.ManyToManyField(Avaliacao, blank=True)

    # relacionar com o endereço
    # relação 1to1 pois um ponto turístico não pode estar em dois locais ao mesmo tempo
    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, primary_key=True
    )

    # retornar nome do local
    def __str__(self):
        return self.nome
