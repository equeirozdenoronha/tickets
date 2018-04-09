import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Usuario(models.Model):
    usuario = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)




class Operador(models.Model):
    operador = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    funcao = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta():
        verbose_name = u'Operador'
        verbose_name_plural = u'Operadores'

    def __str__(self):
        return self.user.first_name

class Chamado(models.Model):
    status = models.IntegerField(max_length=10)
    detalhes = models.CharField(max_length=250)
    tipo = models.CharField(max_length = 30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    dataEHora = models.DateTimeField('dataEHora', default=timezone.now)


    class Meta:
        def __str__(self):
            return self.status

