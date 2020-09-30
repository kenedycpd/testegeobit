from django.test import TestCase
from .forms import LivroForm


class TestLivroForm(TestCase):
    def setUp(self):
        self.form = LivroForm()
        self.resp = self.client.get('livro')

    def test_form_livro(self):
        esperado = ['titulo', 'autor', 'paginas', 'preco', 'data']
        self.assertSequenceEqual(esperado, list(self.form.fields))
