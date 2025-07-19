from django.shortcuts import render


def index(request):

    inicio = {"titulo": "ROUND 6", "subtitulo": "Melhor série da Netflix!", "info": "Round 6 é uma série sul-coreana que segue um grupo de 456 participantes em dificuldades financeiras que aceitam um convite para participar de um jogo mortal com a chance de ganhar 45,6 bilhões de wons. Os jogos são baseados em brincadeiras infantis, mas as apostas são altas e os perdedores enfrentam consequências fatais. A trama explora temas de moralidade e sobrevivência em um ambiente extremo."}

    return render(request, "blog/index.html", {"inicio":inicio})

def atores(request):

    elenco = [
    {"nome": "Seong Gi-hun", "idade": 47, "numero": "Jogador 456", "nascimento": "Seul, Coreia do Sul", "foto": "gi_hun.jpg"},
    {"nome": "Cho Sang-woo", "idade": 46, "numero": "Jogador 218", "nascimento": "Seul, Coreia do Sul", "foto": "sang_woo.jpg"},
    {"nome": "Kang Sae-byeok", "idade": 27, "numero": "Jogadora 067", "nascimento": "Coreia do Norte", "foto": "sae_byeok.jpg"},
    {"nome": "Abdul Ali", "idade": 33, "numero": "Jogador 199", "nascimento": "Paquistão", "foto": "ali.jpg"},
    {"nome": "Oh Il-nam", "idade": 78, "numero": "Jogador 001", "nascimento": "Coreia do Sul", "foto": "il_nam.jpg"},
    {"nome": "Hwang Jun-ho", "idade": 34, "numero": "Policial infiltrado", "nascimento": "Coreia do Sul", "foto": "jun_ho.jpg"},
    {"nome": "O Front Man", "idade": 45, "numero": "Líder do jogo", "nascimento": "Coreia do Sul", "foto": "front_man.jpg"},
    {"nome": "Han Mi-nyeo", "idade": 40, "numero": "Jogadora 212", "nascimento": "Coreia do Sul", "foto": "mi_nyeo.jpg"},
    {"nome": "Jang Deok-su", "idade": 41, "numero": "Jogador 101", "nascimento": "Coreia do Sul", "foto": "deok_su.jpg"},
    {"nome": "Ji-yeong", "idade": 28, "numero": "Jogadora 240", "nascimento": "Coreia do Sul", "foto": "ji_yeong.jpg"},
    {"nome": "Guarda Rosa", "idade": 30, "numero": "Guardião", "nascimento": "Desconhecido", "foto": "guarda_rosa.jpg"},
]

    return render(request, "blog/atores.html", {'elenco':elenco})

def sobre(request):

    texto = {"titulo": "SITE SOBRE ROUND 6", "subtitulo":"um site feito por:", "criadores": "Danilo Lima e Rafael dos Santos"}
    return render(request, "blog/sobre.html", {'texto':texto})
