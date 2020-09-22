from django.urls import include, path
from . import views

urlpatterns = [
    path('livro/', views.livro, name='livro'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('lista/', views.lista, name='lista-livro'),
]