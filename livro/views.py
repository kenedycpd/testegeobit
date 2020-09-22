from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


def livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivroForm()
    return render(request, 'core/livro.html', {'form': form})


def editar(request, id):
    edite = get_object_or_404(Livro, pk=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=edite)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivroForm(instance=edite)
    return render(request, 'core/livro.html', {'form': form})


def deletar(request, id):
    apaga = get_object_or_404(Livro, pk=id)
    apaga.delete()
    return redirect('home')


def lista(request):
    lista = Livro.objects.all()
    return render(request, 'core/list_livro.html', {'lista': lista})
