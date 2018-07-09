from django.urls import path

from . import views

urlpatterns = [
    path('parceiros/', views.home_parceiros, name='home_parceiros'),
    path('parceiros/indicacao/add', views.adiciona_indicacao, name='adiciona_indicacao')
]