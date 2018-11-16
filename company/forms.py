from django.forms import ModelForm, TextInput, URLInput, EmailInput
from .models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'address', 'phone', 'email', 'logo', ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa'}),
            'website': URLInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
