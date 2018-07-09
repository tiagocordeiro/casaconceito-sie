from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect


def home_parceiros(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'index.html')
