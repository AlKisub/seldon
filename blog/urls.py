from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:post>', views.post_edit, name='post_edit'),
    path('point/new/<int:post>', views.point_new, name='point_new'),
    path('point/edit/<int:post>/<int:point>', views.point_edit, name='point_edit'),
    path('point/delete_media', views.delete_media, name='delete_media'),
]
