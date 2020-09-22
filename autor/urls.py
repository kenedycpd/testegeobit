from django.urls import include, path
from . import views

urlpatterns = [
    path('autor/', views.autor, name='autor'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('lista/', views.lista, name='lista-autor'),
]