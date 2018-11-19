from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('dash/', views.dashboard_demo, name='dashboard_demo'),
    path('indicacoes/', views.indicacao_list_dadmin, name='lista_indicacoes'),
    path('indicacao/list/', views.indicacao_list_dadmin, name='indicacao_list'),
    path('indicacao/new/', views.indicacao_add_dadmin, name='indicacao_add'),
    path('indicacao/edit/<pk>/', views.indicacao_edit_dadmin, name='indicacao_edit'),
    path('indicacao/detail/<pk>/', views.indicacao_detail, name='indicacao_detail'),
    path('indicacao/solicitapg/<pk>/', views.indicacao_solicita_pagamento, name='indicacao_solicita_pg'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/avatar/', views.avatar_update, name='avatar_update'),
    path('signup/', views.signup, name='signup'),
    # path('indicacao/add/', views.adiciona_indicacao, name='adiciona_indicacao'),
    # path('indicacao/edit/<pk>/', views.update_indicacao, name='edit_indicacao'),
    # path('indicacoes/', views.lista_indicacoes, name='lista_indicacoes'),
]
