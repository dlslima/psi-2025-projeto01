from django.shortcuts import render

from .models import Ator, Inicio, Sobre


def index(request):
    inicio = Inicio.objects.filter(ativo=True).order_by("-atualizado_em", "-id").first()
    return render(request, "blog/index.html", {"inicio": inicio})


def atores(request):
    elenco = Ator.objects.filter(ativo=True).order_by("ordem", "nome")
    return render(request, "blog/atores.html", {"elenco": elenco})


def sobre(request):
    texto = Sobre.objects.filter(ativo=True).order_by("-atualizado_em", "-id").first()
    return render(request, "blog/sobre.html", {"texto": texto})

