import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Parceiro(models.Model):
    nome_empresa = models.IntegerField(max_length=200)
    nome = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    telefone = models.CharField(max_length=30)
    proposta = models.CharField(max_length=350)
    tipo = models.CharField(max_length=40)

