"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User, Tarefa, Categoria

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "passage_id")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    """Define the admin pages for tarefas."""

    ordering = ["id"]
    list_display = ["titulo", "categoria", "status", "prazo", "usuario"]
    list_filter = ["status", "prazo", "categoria", "usuario"]
    search_fields = ["titulo", "descricao"]
    date_hierarchy = "prazo"

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Define the admin pages for categorias."""

    ordering = ["id"]
    list_display = ["nome", "descricao", "usuario"]
    search_fields = ["nome", "descricao"]
    list_filter = ["usuario"]