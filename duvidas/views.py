# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from duvidas.models import *
from duvidas.serializers import *
import json

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

class PerguntaList(APIView):
    
    def get(self, request, format=None):
        pergunta = Pergunta.objects.all()
        serializer = PerguntaSerializer(pergunta, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PerguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerguntaDetail(APIView):
    """
    Retrieve, update or delete a person instance.
    """

    def get_object(self, pk):
        try:
            return Pergunta.objects.get(pk=pk)
        except Pergunta.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pergunta = self.get_object(pk)
        serializer = PerguntaSerializer(pergunta)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pergunta = self.get_object(pk)
        serializer = PerguntaSerializer(pergunta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pergunta = self.get_object(pk)
        pergunta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriaList(APIView):

    def get(self, request, format=None):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetail(APIView):

    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








