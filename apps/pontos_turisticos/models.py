from django.db import models


# criar model de ponto turistico
class PontoTuristico(models.Model):
    # nome
    nome = models.CharField(max_length=100, help_text="nome do ponto turistico")
    # descrição
    descricao = models.CharField(max_length=250, help_text="descrição breve do local")
    # status do local (para verificar se vai para a listagem ou não)
    # setar default=False
    status = models.BooleanField(default=False, help_text="Aprovado/reprovado")

    # retornar nome do local
    def __str__(self):
        return self.nome
