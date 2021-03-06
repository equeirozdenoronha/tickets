# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from parceiros.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt
def cadastro(request):
    """Tela de cadastro do parceiro"""
    print(request.body)
    if request.method == 'POST':

        # print(request.body)
        data = json.loads(request.body.decode('utf-8'))
        nome_empresa = data['nome_empresa']
        nome = data['nome']
        email = data['email']
        telefone = data['telefone']
        proposta = data['proposta']
        tipo = data['tipo']
        __parceiro = Parceiro(nome_empresa=nome_empresa,nome=nome, email=email,telefone=telefone,proposta=proposta,tipo=tipo)
        __parceiro.save()

        return JsonResponse({'mensagem':'Registrado com sucesso'}, safe=False)

    return JsonResponse({'mensagem':request.body}, safe=False)

@csrf_exempt
def get_parceiros(request):
    if request.method == 'GET':
        parceiros = Parceiro.objects.all().values()
        parceiros_list = list(parceiros)
        return JsonResponse(parceiros_list, safe=False)


