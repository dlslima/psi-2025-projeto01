# Projeto 01 - PSI - 2025

- Data de entrega: 11/07/2025

## Instruções
- Crie um projeto Django de acordo com as instruções do slide 25 da aula 07 [link](https://dvcirilo-ifrn.github.io/psi/slides/aula07.html#25);
- O trabalho deve ser feito em **dupla**, e deve conter *commits* dos dois participantes;
- Apenas um integrante da dupla deve fazer o *fork* desse repositório.

## Como executar (modo desenvolvimento)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/`

## Admin (cadastro do conteúdo dinâmico)

O conteúdo das páginas agora vem do banco via **Models** (sem dados hardcoded como regra). Para cadastrar:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Depois acesse: `http://127.0.0.1:8000/admin/`

Cadastre pelo menos:

- **Início** (`Inicio`): criar 1 registro com `titulo`, `subtitulo`, `info` e `ativo=True`
- **Sobre** (`Sobre`): criar 1 registro com `titulo` (e opcionalmente `subtitulo`, `info`, `criadores`, `foto`, `legenda`)
- **Atores/Personagens** (`Ator`): criar vários registros com `nome`, `idade`, `numero`, `nascimento`, `resumo`, `foto`, `ordem`

### Fotos (campo `foto`)

O campo `foto` deve ser o **nome do arquivo** dentro de `app/static/blog/`.

Exemplos:
- `gi_hun.jpg`
- `squid-game-round-6-temporada.jpg`