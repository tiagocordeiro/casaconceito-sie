from django.forms import ModelForm, TextInput
from .models import Indicacao


class IndicacaoForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', ]

        widgets = {
            'telefone': TextInput(attrs={'class': 'phone', 'type': 'tel'}),
            'celular': TextInput(attrs={'class': 'phone', 'type': 'tel'})
        }


class IndicacaoEditForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', 'status', 'valor', ]
