from django.urls import path
from .views import index
from . import views


urlpatterns = [
    path('lista/', views.lista_produtos, name='lista_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produto/<int:produto_id>/atualizar/', views.atualizar_produto, name='atualizar_produto'),
    path('produto/<int:produto_id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('inicio/', index, name='index'),
    path('localizacao/', views.localizacao, name='localizacao'),
]
