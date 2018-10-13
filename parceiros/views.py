# from django.conf import settings
# from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import IndicacaoForm, IndicacaoEditForm, UserProfileForm, ProfileForm
from .models import Indicacao, UserProfile


@login_required
def home_parceiros(request):
    indicacoes = Indicacao.objects.all().filter(added_by=request.user).order_by('-data_criacao')
    indicacoes_qt = Indicacao.objects.all().filter(added_by=request.user).count()
    indicacoes_ganhas = Indicacao.objects.all() \
        .filter(added_by=request.user) \
        .filter(status='FECHADO').count()
    total_ganho = Indicacao.objects.all() \
        .filter(added_by=request.user) \
        .filter(status='FECHADO').aggregate(Sum('valor'))
    return render(request, 'index.html', {'indicacoes_qt': indicacoes_qt,
                                          'indicacoes_ganhas': indicacoes_ganhas,
                                          'total_ganho': total_ganho['valor__sum'],
                                          'indicacoes': indicacoes, })


@login_required
def dashboard(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None
    indicacoes = Indicacao.objects.all().filter(added_by=request.user).order_by('-data_criacao')
    indicacoes_qt = Indicacao.objects.all().filter(added_by=request.user).count()
    indicacoes_ganhas = Indicacao.objects.all() \
        .filter(added_by=request.user) \
        .filter(status='FECHADO').count()
    total_ganho = Indicacao.objects.all() \
        .filter(added_by=request.user) \
        .filter(status='FECHADO').aggregate(Sum('valor'))
    return render(request, 'dadmin/dashboard.html', {'indicacoes_qt': indicacoes_qt,
                                                     'indicacoes_ganhas': indicacoes_ganhas,
                                                     'total_ganho': total_ganho['valor__sum'],
                                                     'indicacoes': indicacoes,
                                                     'usuario': usuario, })


@login_required
def profile(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None

    return render(request, 'dadmin/profile.html', {'usuario': usuario})


@login_required
def profile_update(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('avatar',))
    formset = ProfileInlineFormset(instance=request.user)

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        formset = ProfileInlineFormset(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            perfil = form.save(commit=False)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=perfil)

            if formset.is_valid():
                perfil.save()
                formset.save()
                # return HttpResponseRedirect('/accounts/profile/')
                return redirect('dashboard')

    else:
        form = ProfileForm(instance=request.user)
        formset = ProfileInlineFormset(instance=request.user)

    return render(request, 'dadmin/profile_update.html', {'form': form,
                                                          'formset': formset,
                                                          'usuario': usuario, })


@login_required
def avatar_update(request):
    try:
        usuario = get_object_or_404(UserProfile)
    except UserProfile.DoesNotExist:
        usuario = None

    perfil = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = UserProfileForm(instance=perfil)

    return render(request, 'dadmin/avatar_update.html', {'form': form,
                                                         'usuario': usuario, })


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
def update_indicacao(request, pk):
    indicacao = get_object_or_404(Indicacao, pk=pk)

    if request.method == 'POST':
        form = IndicacaoEditForm(request.POST, instance=indicacao)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "A indicação foi atualizada")

        except Exception as e:
            # pass
            messages.warning(request, 'Ocorreu um erro ao atualizar: {}'.format(e))

    else:
        form = IndicacaoEditForm(instance=indicacao)

    contex = {
        'form': form,
        'indicacao': indicacao,
    }

    return render(request, 'indicacoes/indicacao_edit.html', contex)


@login_required
def lista_indicacoes(request):
    if request.user.is_superuser:
        indicacoes = Indicacao.objects.all().order_by('-data_criacao')
    else:
        indicacoes = Indicacao.objects.all().filter(added_by=request.user).order_by('-data_criacao')

    return render(request, 'indicacoes/list.html', {'indicacoes': indicacoes})


@login_required
def dashboard_demo(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None
    indicacoes = Indicacao.objects.all().filter(added_by=request.user).order_by('-data_criacao')
    indicacoes_qt = Indicacao.objects.all().filter(added_by=request.user).count()
    indicacoes_ganhas = Indicacao.objects.all() \
        .filter(added_by=request.user) \
        .filter(status='FECHADO').count()
    total_ganho = Indicacao.objects.all() \
        .filter(added_by=request.user) \
        .filter(status='FECHADO').aggregate(Sum('valor'))
    return render(request, 'dadmin/dashboard_demo.html', {'indicacoes_qt': indicacoes_qt,
                                                          'indicacoes_ganhas': indicacoes_ganhas,
                                                          'total_ganho': total_ganho['valor__sum'],
                                                          'indicacoes': indicacoes,
                                                          'usuario': usuario, })


@login_required
def indicacao_list_dadmin(request):
    if request.user.is_superuser:
        indicacoes = Indicacao.objects.all().order_by('-data_criacao')
    else:
        indicacoes = Indicacao.objects.all().filter(added_by=request.user).order_by('-data_criacao')

    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None

    return render(request, 'dadmin/indicacao_list.html', {'indicacoes': indicacoes,
                                                          'usuario': usuario, })


@login_required
def indicacao_add_dadmin(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        form = IndicacaoForm(request.POST)
        if form.is_valid():
            indicacao = form.save(commit=False)
            indicacao.added_by = request.user
            indicacao.save()
            return redirect(indicacao_list_dadmin)

    else:
        form = IndicacaoForm()

    return render(request, 'dadmin/indicacao_new.html', {'form': form,
                                                         'usuario': usuario, })


@login_required
def indicacao_edit_dadmin(request, pk):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None

    indicacao = get_object_or_404(Indicacao, pk=pk)

    if request.method == 'POST':
        form = IndicacaoEditForm(request.POST, instance=indicacao)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "A indicação foi atualizada")

        except Exception as e:
            messages.warning(request, 'Ocorreu um erro ao atualizar: {}'.format(e))

    else:
        form = IndicacaoEditForm(instance=indicacao)

    contex = {
        'form': form,
        'indicacao': indicacao,
        'usuario': usuario,
    }

    return render(request, 'dadmin/indicacao_edit.html', contex)