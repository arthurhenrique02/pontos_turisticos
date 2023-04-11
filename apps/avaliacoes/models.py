from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User


# criar model
class Avaliacao(models.Model):
    # usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # avaliação
    estrelas = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        # validação, habilitar numeros entre 0.00 e 10.00
        validators=[
            MinValueValidator(Decimal("0.00")),
            MaxValueValidator(Decimal("10.00")),
        ],
    )

    def __str__(self):
        return f"{self.user.username} {self.estrelas}"
