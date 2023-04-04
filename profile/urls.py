from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.account_page, name='account_page'),
    path('profiles/', views.account_profiles, name='account_profiles'),
    path('account_edit/', views.account_edit, name='account_edit'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path('change_password/', views.change_password, name='change_password'),
]
