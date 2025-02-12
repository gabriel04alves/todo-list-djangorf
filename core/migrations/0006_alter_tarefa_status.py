# Generated by Django 5.1.2 on 2025-02-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_categoria_tarefa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="status",
            field=models.CharField(
                choices=[("pendente", "Pendente"), ("em_andamento", "Em Andamento"), ("concluida", "Concluida")],
                default="pendente",
                max_length=15,
            ),
        ),
    ]
