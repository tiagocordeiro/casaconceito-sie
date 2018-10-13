from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Indicacao


class IndicacaoForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', ]

        widgets = {
            'cliente': TextInput(attrs={'class': 'form-control', 'placeholder': 'Cliente'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': TextInput(attrs={'class': 'form-control phone', 'type': 'tel', }),
            'celular': TextInput(attrs={'class': 'form-control phone', 'type': 'tel', }),
            'descricao': Textarea(attrs={'class': 'form-control', })
        }


class IndicacaoEditForm(ModelForm):
    class Meta:
        model = Indicacao
        fields = ['cliente', 'descricao', 'email', 'telefone',
                  'celular', 'status', 'valor', ]

        widgets = {
            'cliente': TextInput(attrs={'class': 'form-control', 'placeholder': 'Cliente'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefone': TextInput(attrs={'class': 'form-control phone', 'type': 'tel', }),
            'celular': TextInput(attrs={'class': 'form-control phone', 'type': 'tel', }),
            'descricao': Textarea(attrs={'class': 'form-control', }),
            'status': Select(attrs={'class': 'form-control', }),
            'valor': TextInput(attrs={'class': 'form-control', }),
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
