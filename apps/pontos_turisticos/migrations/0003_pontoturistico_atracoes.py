# Generated by Django 4.2 on 2023-04-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("atracoes", "0001_initial"),
        ("pontos_turisticos", "0002_alter_pontoturistico_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="pontoturistico",
            name="atracoes",
            field=models.ManyToManyField(to="atracoes.atracao"),
        ),
    ]
