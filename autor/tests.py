from django.test import TestCase
from .models import Autor


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



class TesForm(TestCase):
    def setUp(self):
        
