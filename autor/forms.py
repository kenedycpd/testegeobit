from django.forms import ModelForm
from .models import Autor
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

    def clean(self):
        a = self.cleaned_data['nome']
        if Autor.objects.filter(nome=a).exists():
            raise ValidationError(_(' esse autor já existe no sistema!'))
        return a
