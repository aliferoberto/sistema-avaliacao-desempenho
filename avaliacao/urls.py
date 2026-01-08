from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('avaliacoes/', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacoes/nova/', views.criar_avaliacao, name='criar_avaliacao'),
    path('avaliacoes/<int:id>/', views.detalhe_avaliacao, name='detalhe_avaliacao'),
    path('avaliacoes/<int:avaliacao_id>/nota/', views.adicionar_nota, name='adicionar_nota'),
    path('avaliacoes/excluir/<int:id>/', views.excluir_avaliacao, name='excluir_avaliacao'),
]