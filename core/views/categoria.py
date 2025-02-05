from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models.aggregates import Sum
from django_filters.rest_framework import DjangoFilterBackend

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
        if usuario.is_superuser:
            return Categoria.objects.all()
        if usuario.groups.filter(name="admin"):
            return Categoria.objects.all()
        return Categoria.objects.filter(usuario=usuario)

    def perform_create(self, serializer):
        """Associate the user with the categoria."""
        serializer.save(usuario=self.request.user)

    @action(detail=False, methods=["get"])
    def total_por_categoria(self, request):
        """Return the total of categorias per usuario."""
        total_por_categoria = (
            Categoria.objects.values("usuario__username")
            .annotate(total=Sum("id"))
            .order_by("usuario__username")
        )
        return Response(total_por_categoria, status=status.HTTP_200_OK)