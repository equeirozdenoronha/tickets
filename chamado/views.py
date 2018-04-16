from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from chamado.models import *
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'chamado/index.html', {})

def room(request, room_name):

    return render(request, 'chamado/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
#
# def listar_chamados(request, status, usuario, operador):
#
#     pass
#
# def statusChamado(request, status):
#     pass
#
# def efetuar_chamado(request):
#     pass
