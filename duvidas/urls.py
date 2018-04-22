from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from duvidas import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/perguntas/', views.PerguntaList.as_view()),
    path('api/perguntas/<int:pk>/', views.PerguntaDetail.as_view()),
    path('api/categorias/', views.CategoriaList.as_view()),
    path('api/categorias/<int:pk>/', views.CategoriaDetail.as_view())
]
