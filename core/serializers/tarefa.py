from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    DateTimeField,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)
from datetime import date
from core.models import Tarefa


class TarefaSerializer(ModelSerializer):
    usuario = CharField(source="usuario.username", read_only=True)
    categoria = CharField(source="categoria.nome")
    criado_em = DateTimeField(read_only=True)

    class Meta:
        model = Tarefa
        fields = "__all__"


class TarefaCreateUpdateSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Tarefa
        fields = "__all__"

    def validate_prazo(self, prazo):
        if prazo < date.today():
            raise ValidationError("A data de prazo não pode ser no passado.")
        return prazo


class TarefaListSerializer(ModelSerializer):
    categoria = CharField(source="categoria.nome", read_only=True)
    status_display = SerializerMethodField()

    def get_status_display(self, instance):
        return instance.get_status_display()

    class Meta:
        model = Tarefa
        fields = "__all__"
