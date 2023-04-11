from django.db import models

from apps.atracoes.models import Atracao
from apps.comentarios.models import Comentario
from apps.avaliacoes.models import Avaliacao


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
    atracoes = models.ManyToManyField(Atracao)

    # relacionar com comentarios
    comentarios = models.ManyToManyField(Comentario)

    # relacionar com avaliações
    avaliacoes = models.ManyToManyField(Avaliacao)

    # retornar nome do local
    def __str__(self):
        return self.nome
