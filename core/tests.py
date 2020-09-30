from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_home(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def teste_link_home(self):
        self.assertContains(self.response, 'href="#"')
