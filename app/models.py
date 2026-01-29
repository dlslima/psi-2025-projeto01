from django.db import models

class Inicio(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    info = models.TextField()

    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Início"
        verbose_name_plural = "Início"

    def __str__(self) -> str:
        return self.titulo


class Ator(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.PositiveIntegerField()
    numero = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=200)
    resumo = models.TextField()
    foto = models.CharField(
        max_length=255,
        help_text="Nome do arquivo em app/static/blog/ (ex.: gi_hun.jpg)",
    )

    ordem = models.PositiveIntegerField(default=0, help_text="Ordenação na página.")
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ator/Personagem"
        verbose_name_plural = "Atores/Personagens"
        ordering = ["ordem", "nome"]

    def __str__(self) -> str:
        return self.nome


class Sobre(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)

    foto = models.CharField(
        max_length=255,
        blank=True,
        help_text="Nome do arquivo em app/static/blog/ (ex.: squid-game-round-6-temporada.jpg)",
    )
    legenda = models.CharField(max_length=255, blank=True)
    info = models.TextField(blank=True)
    criadores = models.CharField(max_length=255, blank=True)

    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Sobre"

    def __str__(self) -> str:
        return self.titulo
