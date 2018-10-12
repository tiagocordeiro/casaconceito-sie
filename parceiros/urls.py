from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_parceiros, name='home_parceiros'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dash/', views.dashboard_demo, name='dashboard_demo'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/avatar/', views.avatar_update, name='avatar_update'),
    path('indicacao/add/', views.adiciona_indicacao, name='adiciona_indicacao'),
    path('indicacao/edit/<pk>/', views.update_indicacao, name='edit_indicacao'),
    path('indicacoes/', views.lista_indicacoes, name='lista_indicacoes'),
]
