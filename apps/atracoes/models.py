from django.db import models


# criar model para atração
class Atracao(models.Model):
    # nome
    nome = models.CharField(max_length=100, help_text="nome da atração")
    # descricao
    descricao = models.CharField(max_length=250, help_text="breve descrição")
    # horario de abertura
    horario_abertura = models.TimeField()
    # horario de fechamento
    horario_fechamento = models.TimeField()
    # idade minima
    idade_min = models.IntegerField(help_text="idade minima")

    # retornar nome
    def __str__(self):
        return self.nome
