from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/editar/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('projetos/excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),
]

