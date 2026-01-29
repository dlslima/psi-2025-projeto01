from django.contrib import admin

from .models import Ator, Inicio, Sobre


@admin.register(Inicio)
class InicioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo", "ativo", "criado_em", "atualizado_em")
    list_filter = ("ativo", "criado_em")
    search_fields = ("titulo", "subtitulo", "info")
    readonly_fields = ("criado_em", "atualizado_em")


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ("ordem", "nome", "numero", "idade", "ativo", "criado_em")
    list_display_links = ("nome",)
    list_filter = ("ativo", "criado_em")
    search_fields = ("nome", "numero", "nascimento", "resumo")
    ordering = ("ordem", "nome")
    readonly_fields = ("criado_em", "atualizado_em")
    list_editable = ("ordem", "ativo")


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo", "ativo", "criado_em", "atualizado_em")
    list_filter = ("ativo", "criado_em")
    search_fields = ("titulo", "subtitulo", "info", "criadores")
    readonly_fields = ("criado_em", "atualizado_em")
