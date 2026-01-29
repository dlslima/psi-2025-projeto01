from django.contrib import admin

from .models import Ator, Inicio, Sobre


@admin.register(Inicio)
class InicioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo", "ativo", "atualizado_em")
    list_filter = ("ativo",)
    search_fields = ("titulo", "subtitulo", "info")


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ("ordem", "nome", "numero", "idade", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome", "numero", "nascimento", "resumo")
    ordering = ("ordem", "nome")


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo", "ativo", "atualizado_em")
    list_filter = ("ativo",)
    search_fields = ("titulo", "subtitulo", "info", "criadores")
