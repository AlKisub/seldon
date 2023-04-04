from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_new'),
    path('<int:post>/edit', views.post_edit, name='post_edit'),
    path('<int:post>/create/', views.point_create, name='point_new'),
    path('<int:post>/edit/<int:point>', views.point_edit, name='point_edit'),
    path('delete_media/', views.delete_media, name='delete_media'),
]
