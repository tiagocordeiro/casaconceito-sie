from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Indicacao


class IndicacaoForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', ]

        widgets = {
            'telefone': TextInput(attrs={'class': 'phone', 'type': 'tel', }),
            'celular': TextInput(attrs={'class': 'phone', 'type': 'tel', })
        }


class IndicacaoEditForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', 'status', 'valor', ]

        widgets = {
            'telefone': TextInput(attrs={'class': 'phone', 'type': 'tel', }),
            'celular': TextInput(attrs={'class': 'phone', 'type': 'tel', })
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile

        fields = ['avatar', ]
        # fields = '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
