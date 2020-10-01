from django.test import TestCase
from .models import Autor
from django.urls import reverse
from .forms import AutorForm


class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(
            nome='kenedy',
            idade=34,
            email='kenedy@santos.com',
            telefone=91343877

        )

    def test_retorna_str(self):
        p1 = Autor.objects.get(nome='kenedy')
        idade = 34
        email = 'kenedy@santos.com'
        telefone = 91343877

        self.assertEqual(p1.__str__(), 'kenedy')
        self.assertEqual(idade, 34)
        self.assertEqual(email, 'kenedy@santos.com')
        self.assertEqual(telefone, 91343877)


class TesView(TestCase):

    def test_view_bio(self):
        response = self.client.get(reverse('bio'))
        self.assertEquals(response.status_code, 200)

    def test_template_bio(self):
        response = self.client.get(reverse('bio'))
        self.assertTemplateUsed(response, 'core/bio.html')

    def test_form_bio_view(self):
        response = self.client.get(reverse('form_bio_view'))
        self.assertEquals(response.status_code, 200)

    def test_form(self):
        response = self.client.get(reverse('form_bio'))
        self.assertTemplateUsed(response, 'core/form_bio.html')

    def test_form_autor(self):
        form = AutorForm(data={
            'nome': 'kenedy',
            'idade': 34,
            'email': 'kenedy@santos.com',
            'telefone': 91343877
        })
        self.assertTrue(form.is_valid())
