# Generated by Django 4.2 on 2023-04-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dados", models.TextField(verbose_name="Digite o endereço")),
                ("cidade", models.CharField(help_text="Cidade", max_length=250)),
                ("estado", models.CharField(help_text="Estado", max_length=70)),
                ("pais", models.CharField(help_text="País", max_length=70)),
                ("latitude", models.IntegerField(blank=True, null=True)),
                ("longitude", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
