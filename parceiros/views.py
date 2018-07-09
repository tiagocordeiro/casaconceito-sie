from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .forms import IndicacaoForm
from .models import Indicacao


def home_parceiros(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'index.html')

@login_required
def adiciona_indicacao(request):
    if request.method == 'POST':
        form = IndicacaoForm(request.POST)
        if form.is_valid():
            indicacao = form.save(commit=False)
            indicacao.added_by = request.user
            indicacao.save()
            return redirect(lista_indicacoes)

    else:
        form = IndicacaoForm()

    return render(request, 'indicacoes/new.html', {'form': form})

@login_required
def lista_indicacoes(request):
    if request.user.is_superuser:
        indicacoes = Indicacao.objects.all().order_by('-data_criacao')
    else:
        indicacoes = Indicacao.objects.all().filter(added_by=request.user).order_by('-data_criacao')

    return render(request, 'indicacoes/list.html', {'indicacoes': indicacoes})
