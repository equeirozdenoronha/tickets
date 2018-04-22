from rest_framework import serializers
from duvidas.models import *

class PerguntaSerializer(serializers.Serializer):
    pergunta = serializers.CharField(max_length=250)
    resposta = serializers.CharField(max_length=500)
    categorias = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):

        return Pergunta.objects.create(**validated_data)

    class Meta:
        model = Pergunta
        fields = ('pergunta', 'resposta', 'categorias')

class CategoriaSerializer(serializers.Serializer):
    nomeCategoria = serializers.CharField(max_length=30)

    def create(self, validated_data):

        return Categoria.objects.create(**validated_data)

    class Meta:
        model = Categoria
        fields = ('nomeCategoria',)