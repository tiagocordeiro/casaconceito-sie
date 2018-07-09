from django.urls import path

from . import views

urlpatterns = [
    path('parceiros/', views.home_parceiros, name='home_parceiros'),
]