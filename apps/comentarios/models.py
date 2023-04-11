from django.db import models
from django.contrib.auth.models import User

from apps.avaliacoes.models import Avaliacao


# criar model
class Comentario(models.Model):
    # usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # comentario
    comentario = models.TextField()

    # data (auto incrementar)
    data = models.DateTimeField(auto_now_add=True)

    # status (comentario aprovado ou não)
    status = models.BooleanField(default=True)

    # relacionar com avaliação
    avaliacao = models.ForeignKey(
        Avaliacao, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}, {self.comentario}"
