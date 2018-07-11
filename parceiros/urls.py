from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_parceiros, name='home_parceiros'),
    path('indicacao/add', views.adiciona_indicacao, name='adiciona_indicacao'),
    path('indicacao/edit/<pk>', views.update_indicacao, name='edit_indicacao'),
    path('indicacoes', views.lista_indicacoes, name='lista_indicacoes'),
]
