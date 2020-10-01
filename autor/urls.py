from django.urls import include, path
from . import views

urlpatterns = [
    path('autor/', views.autor, name='autor'),
    path('bio/', views.bio, name='bio'),
    path('form_bio_view/', views.form_bio_view, name='form_bio_view'),
    path('form_bio/', views.form_bio, name='form_bio'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('lista/', views.lista, name='lista-autor'),
]
