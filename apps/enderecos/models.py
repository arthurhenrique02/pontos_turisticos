from django.db import models


# criar model
class Endereco(models.Model):
    # dados (rua, bairro, ..., vila, nome, ....)
    # feito desta forma pois nem todos os locais atendem por rua, bairro
    dados = models.TextField("Digite o endereço")

    # cidade
    cidade = models.CharField(max_length=250, help_text="Cidade")

    # estado
    estado = models.CharField(max_length=70, help_text="Estado")

    # país
    pais = models.CharField(max_length=70, help_text="País")

    # latitude, colocar como opcional (poderá ser nulo e em branco)
    latitude = models.IntegerField(null=True, blank=True)

    # longitude, colocar como opcional (poderá ser nulo e em branco)
    longitude = models.IntegerField(null=True, blank=True)

    # retornar endereço/dados
    def __str__(self):
        return self.dados
