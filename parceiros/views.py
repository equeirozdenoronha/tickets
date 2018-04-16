# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.shortcuts import redirect

from parceiros.models import *


def cadastro(request):
    """Tela de cadastro do parceiro"""
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.nomeEmpresa = request.POST.get('nome_empresa')
            user.nomeDono = user.nome_dono
            user.emailDono = user.email
            user.telefone = user.telefone
            user.Desc = user.descricao
            user.save()

            parceiro = Parceiro.objects.create(
                user=user
            )
            parceiro.save()

            messages.success(request, _('Registrado com sucesso!'))
            return redirect('dashboard:login')
        else:
            messages.error(request, _('Ooops! Verifique os erros abaixo.'))
    else:
        user_form = UserForm()

    return render(request, 'dashboard/cadastro.html', {
        'user_form': user_form,
        'CODE': request.GET.get('referral', ''),
    })
