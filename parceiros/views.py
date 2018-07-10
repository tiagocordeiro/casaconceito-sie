from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .forms import IndicacaoForm
from .models import Indicacao


@login_required
def home_parceiros(request):
    indicacoes_qt = Indicacao.objects.all().filter(added_by=request.user).count()
    indicacoes_ganhas = Indicacao.objects.all()\
        .filter(added_by=request.user)\
        .filter(status='FECHADO').count()
    total_ganho = Indicacao.objects.all()\
        .filter(added_by=request.user)\
        .filter(status='FECHADO').aggregate(Sum('valor'))
    return render(request, 'index.html', {'indicacoes_qt': indicacoes_qt,
                                          'indicacoes_ganhas': indicacoes_ganhas,
                                          'total_ganho': total_ganho['valor__sum']})


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
