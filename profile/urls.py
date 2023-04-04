from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path('change_password/', views.change_password, name='change_password'),
]
