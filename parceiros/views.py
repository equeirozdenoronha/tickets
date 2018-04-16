# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from parceiros.models import *
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def cadastro(request):
    """Tela de cadastro do parceiro"""
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        nome_empresa = data['nome_empresa']
        nome = data['nome']
        email = data['email']
        telefone = data['telefone']
        proposta = data['proposta']
        tipo = data['tipo']
        return JsonResponse({'mensagem':'Registrado com sucesso'}, safe=False)

    return JsonResponse({'mensagem':'Erro'} , safe=False)
