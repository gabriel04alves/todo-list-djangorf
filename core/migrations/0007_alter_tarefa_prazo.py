# Generated by Django 5.1.2 on 2025-02-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_tarefa_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="prazo",
            field=models.DateTimeField(),
        ),
    ]
