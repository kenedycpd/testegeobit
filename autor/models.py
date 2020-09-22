from django.db import models


class Autor(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)

    class Meta:
        verbose_name = 'Autor'

    def __str__(self):
        return self.nome
