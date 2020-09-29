from django.db import models


class Autor(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    idade = models.IntegerField('idade')
    email = models.EmailField('email')
    telefone = models.CharField('telefone', max_length=14)

    class Meta:
        verbose_name = 'Autor'

    def __str__(self):
        return self.nome
