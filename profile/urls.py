from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.account_page, name='account_page'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
]
