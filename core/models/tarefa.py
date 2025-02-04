from django.db import models
from .user import User
from .categoria import Categoria

class Tarefa(models.Model):
    class StatusTarefa(models.TextChoices):
        PENDENTE = "pendente"
        EM_ANDAMENTO = "em_andamento"
        CONCLUIDA = "concluida"
    
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=15,choices=StatusTarefa.choices, default=StatusTarefa.PENDENTE)
    prazo = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="tarefas")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tarefas")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} | {self.categoria} | "