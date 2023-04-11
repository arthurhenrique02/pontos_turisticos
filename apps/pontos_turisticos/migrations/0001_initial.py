# Generated by Django 4.2 on 2023-04-11 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("atracoes", "0001_initial"),
        ("avaliacoes", "0003_alter_avaliacao_estrelas"),
        ("comentarios", "0003_alter_comentario_avaliacao"),
        ("enderecos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PontoTuristico",
            fields=[
                (
                    "nome",
                    models.CharField(
                        help_text="nome do ponto turistico", max_length=100
                    ),
                ),
                (
                    "descricao",
                    models.CharField(
                        help_text="descrição breve do local", max_length=250
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=False, help_text="Aprovado/reprovado"),
                ),
                (
                    "endereco",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="enderecos.endereco",
                    ),
                ),
                ("atracoes", models.ManyToManyField(blank=True, to="atracoes.atracao")),
                (
                    "avaliacoes",
                    models.ManyToManyField(blank=True, to="avaliacoes.avaliacao"),
                ),
                (
                    "comentarios",
                    models.ManyToManyField(blank=True, to="comentarios.comentario"),
                ),
            ],
        ),
    ]
