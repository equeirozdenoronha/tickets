from django.db import models

class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=30)
    def __str__(self):
        return self.nomeCategoria
class Pergunta(models.Model):
    pergunta = models.CharField(max_length=250)
    resposta = models.CharField(max_length=2000)
    categorias = models.ManyToManyField(Categoria, null=True, related_name="categorias")
    def __str__(self):
        return self.pergunta



