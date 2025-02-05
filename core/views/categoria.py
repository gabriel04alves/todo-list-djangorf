import stat
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models.aggregates import Sum
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    """ViewSet for categorias."""

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["nome"]
    search_fields = ["nome", "descricao"]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser or usuario.groups.filter(name="admin"):
            return Categoria.objects.all()
        else:
            return Categoria.objects.filter(usuario=usuario)

    def perform_create(self, serializer):
        """Associate the user with the categoria."""
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=["get"])
    def total_por_categoria(self, request):
        """Return the total of tarefas per categoria for the authenticated user."""
        usuario = request.user
        if usuario.is_superuser or usuario.groups.filter(name="admin").exists():
            categorias = Categoria.objects.all()
        else:
            categorias = Categoria.objects.filter(usuario=usuario)

        total = categorias.annotate(total_tarefas=Count("tarefas")).values("nome", "total_tarefas")
        return Response(total, status=status.HTTP_200_OK)
