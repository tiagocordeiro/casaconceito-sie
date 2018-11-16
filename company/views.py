from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from parceiros.models import UserProfile
from .forms import CompanyForm
from .models import Company


@login_required
@user_passes_test(lambda u: u.groups.filter(name='CompanyAdmin').count() == 1 or u.is_staff)
def company_details(request):
    try:
        usuario = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        usuario = None

    company = Company.objects.all().last()

    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = CompanyForm(instance=company)

    context = {
        'usuario': usuario,
        'company': company,
        'form': form,
    }

    return render(request, 'dadmin/company/details.html', context)
