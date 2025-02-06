from django.db import models
from .user import User
from .categoria import Categoria
import datetime


class Tarefa(models.Model):
    class TaskStatus(models.TextChoices):
        PENDENTE = "pendente"
        EM_ANDAMENTO = "em_andamento"
        CONCLUIDA = "concluida"
        ATRASADA = "atrasada"

    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=TaskStatus.choices, default=TaskStatus.PENDENTE)
    prazo = models.DateField()
    categorias = models.ManyToManyField(Categoria, related_name="tarefas")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tarefas")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} | {', '.join([categoria.nome for categoria in self.categorias.all()])}"
