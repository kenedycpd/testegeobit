from django.contrib import admin
from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'paginas', 'preco', 'data')
    search_fields = ('nome', 'autor', 'data')
