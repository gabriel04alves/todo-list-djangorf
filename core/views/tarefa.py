from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models.aggregates import Sum
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Tarefa
from core.serializers import TarefaSerializer
from core.serializers import TarefaCreateUpdateSerializer


class TarefaViewSet(ModelViewSet):
    """ViewSet for tarefas."""

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Tarefa.objects.all()
        if usuario.groups.filter(name="admin"):
            return Tarefa.objects.all()
        return Tarefa.objects.filter(usuario=usuario)

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["status", "prazo", "categorias"]
    search_fields = ["titulo", "descricao"]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return TarefaCreateUpdateSerializer
        return TarefaSerializer

    def perform_create(self, serializer):
        """Associate the user with the tarefa."""
        serializer.save(usuario=self.request.user)
