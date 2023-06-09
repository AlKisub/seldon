from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:news>/edit/', views.news_edit, name='news_edit'),
    path('create/', views.news_create, name='news_create'),
]
