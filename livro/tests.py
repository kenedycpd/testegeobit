from django.test import TestCase, Client
from .forms import LivroForm
from django.urls import reverse_lazy


class TestLivroForm(TestCase):
    def setUp(self):
        self.form = LivroForm()

    def test_form_livro(self):
        esperado = ['titulo', 'autor', 'paginas', 'preco', 'data']
        self.assertSequenceEqual(esperado, list(self.form.fields))


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('livro')
        self.lista = reverse_lazy('lista-livro')

    def test_url(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_lista(self):
        response_lista = self.client.get(self.lista)

        self.assertTemplateUsed(response_lista, 'core/list_livro.html')
