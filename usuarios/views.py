from django.shortcuts import render
from visitantes.models import Visitante


def index(request):

    todos_visitantes = Visitante.objects.all()
    
    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes
    }

    return render(request, 'index.html', context)

def informacoes_visitante(request, id):

    context = {
        "nome_pagina": "Informações do visitante",
    }

    return render(request, 'informacoes_visitante.html', context)
