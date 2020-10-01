from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Autor
from .forms import AutorForm


def autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'core/autor.html', {'form': form})


def editar(request, id):
    edite = get_object_or_404(Autor, pk=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=edite)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm(instance=edite)
    return render(request, 'core/autor.html', {'form': form})


def deletar(request, id):
    apaga = get_object_or_404(Autor, pk=id)
    apaga.delete()
    return redirect('home')


def lista(request, id=id):
    lista = Autor.objects.all()
    return render(request, 'core/list_autor.html', {'lista': lista})


def bio(request):
    return render(request, 'core/bio.html', {})


def form_bio_view(self):
    return HttpResponse('ok')
    pass


def form_bio(request):
    return render(request, 'core/form_bio.html')
