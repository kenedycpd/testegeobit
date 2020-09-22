from django.db import models
from autor.models import Autor
from django.core.validators import MinValueValidator
from decimal import Decimal


class Livro(models.Model):
    titulo = models.CharField('Titulo', max_length=150, blank=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False)
    paginas = models.IntegerField('Quantidade de Paginas', blank=False)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))])
    data = models.DateField('Data', blank=False)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo
