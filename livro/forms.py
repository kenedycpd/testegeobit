from django.forms import ModelForm
from .models import Livro
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

    def clean(self):
        t = self.cleaned_data['titulo']
        if Livro.objects.filter(titulo=t).exists():
            raise ValidationError(_(' esse livro já existe no sistema!'))
        return t
