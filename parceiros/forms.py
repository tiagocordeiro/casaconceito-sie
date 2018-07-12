from django.forms import ModelForm
from .models import Indicacao


class IndicacaoForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', ]


class IndicacaoEditForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', 'status', 'valor', ]
