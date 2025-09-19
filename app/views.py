from django.shortcuts import render


def index(request):

    inicio = {"titulo": "ROUND 6", "subtitulo": "A melhor série da Netflix!", "info": "Round 6 é uma série sul-coreana que segue um grupo de 456 participantes em dificuldades financeiras que aceitam um convite para participar de um jogo mortal com a chance de ganhar 45,6 bilhões de wons. Os jogos são baseados em brincadeiras infantis, mas as apostas são altas e os perdedores enfrentam consequências fatais. A trama explora temas de moralidade e sobrevivência em um ambiente extremo. Round 6 foi lançada em 17 de Setembro de 2021 pela Netflix, criada por Hwang Dong-hyunk. A série se tornou um fenômeno mundial, alcançando mais de 142 milhões de telespectadores no primeiro mês, o que a tornou a produção mais vista da história da plataforma. Além disso, recebeu indicações e prêmios importantes, incluindo o Emmy de Melhor Ator para Lee Jung-jae."}

    return render(request, "blog/index.html", {"inicio":inicio})

def atores(request):

    elenco = [
    {"nome": "Seong Gi-hun (Lee Jung-jae)", "idade": 47, "numero": "Jogador 456", "nascimento": "Seul, Coreia do Sul", "resumo": "Um apostador divorciado e endividado que entra no jogo para ganhar dinheiro e recuperar a custódia da filha.", "foto": "gi_hun.jpg"},
    {"nome": "Cho Sang-woo (Park Hae-soo)", "idade": 46, "numero": "Jogador 218", "nascimento": "Seul, Coreia do Sul", "resumo": "Ex-executivo de investimentos inteligente, mas desonesto, que é procurado pela polícia.", "foto": "sang_woo.jpg"},
    {"nome": "Kang Sae-byeok (Jung Ho-yeon)", "idade": 27, "numero": "Jogadora 067", "nascimento": "Coreia do Norte", "resumo": "Uma jovem determinada que quer resgatar a família e trazer a mãe para a Coreia do Sul.", "foto": "sae_byeok.jpg"},
    {"nome": "Abdul Ali (Anupam Tripathi)", "idade": 33, "numero": "Jogador 199", "nascimento": "Paquistão", "resumo": "Trabalhador estrangeiro que entra no jogo para sustentar a família.", "foto": "ali.jpg"},
    {"nome": "Oh Il-nam (Oh Yeong-su)", "idade": 78, "numero": "Jogador 001", "nascimento": "Coreia do Sul", "resumo": "Um idoso com um tumor cerebral que parece frágil, mas esconde segredos.", "foto": "il_nam.jpg"},
    {"nome": "Hwang Jun-ho (Wi Ha-joon)", "idade": 34, "numero": "Policial infiltrado", "nascimento": "Coreia do Sul", "resumo": "Um policial infiltrado que busca o irmão desaparecido.", "foto": "jun_ho.jpg"},
    {"nome": "O Front Man (Lee Byung-hun)", "idade": 45, "numero": "Líder do jogo", "nascimento": "Coreia do Sul", "resumo": "Misterioso líder mascarado que supervisiona os jogos.", "foto": "front_man.jpg"},
    {"nome": "Han Mi-nyeo (Kim Joo-ryoung)", "idade": 40, "numero": "Jogadora 212", "nascimento": "Coreia do Sul", "resumo": "Mulher manipuladora e imprevisível que faz alianças temporárias.", "foto": "mi_nyeo.jpg"},
    {"nome": "Jang Deok-su (Heo Sung-Tae)", "idade": 41, "numero": "Jogador 101", "nascimento": "Coreia do Sul", "resumo": "Criminoso violento que usa a força para sobreviver.", "foto": "deok_su.jpg"},
    {"nome": "Ji-yeong (Lee Yoo-mi)", "idade": 28, "numero": "Jogadora 240", "nascimento": "Coreia do Sul", "resumo": "Jovem com um passado trágico que forma uma conexão emocional com Sae-byeok.", "foto": "ji_yeong.jpg"},
    {"nome": "Guarda Rosa", "idade": 30, "numero": "Guardião", "nascimento": "Desconhecido", "resumo": "Guardiões mascarados que fiscalizam os jogadores.", "foto": "guarda_rosa.jpg"},
]

    return render(request, "blog/atores.html", {'elenco':elenco})

def sobre(request):

    texto = {"titulo": "SITE SOBRE ROUND 6", "foto": "squid-game-round-6-temporada.jpg", "info": "Neste site você encontrará: Sinopse rápida da trama, Elenco, personagens principais e suas informações, tudo em um só lugar para fãs e amantes de Round 6!", "subtitulo":"Um site feito por:", "criadores": "Danilo Lima e Rafael dos Santos"}
    return render(request, "blog/sobre.html", {'texto':texto})

