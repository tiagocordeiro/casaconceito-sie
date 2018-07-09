from django.shortcuts import render


def home_parceiros(request):
    return render(request, 'index.html')