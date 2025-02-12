# Generated by Django 5.1.2 on 2025-02-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_remove_tarefa_categoria_tarefa_categorias"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="status",
            field=models.CharField(
                choices=[
                    ("pendente", "Pendente"),
                    ("em_andamento", "Em Andamento"),
                    ("concluida", "Concluida"),
                    ("atrasada", "Atrasada"),
                ],
                default="pendente",
                max_length=15,
            ),
        ),
    ]
