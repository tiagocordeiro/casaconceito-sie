from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .forms import IndicacaoForm


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
            return render(request, 'indicacoes/new.html', {'form': form})

    else:
        form = IndicacaoForm()

    return render(request, 'indicacoes/new.html', {'form': form})
