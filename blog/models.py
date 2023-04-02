from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    map_href = models.TextField(blank=True, null=True, default='', verbose_name='Виджет с картой маршрута')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edit_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')

    def publish(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Point(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Связанный пост', null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    sequence_number = models.PositiveIntegerField(verbose_name='Порядковый номер')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    map_href = models.TextField(blank=True, null=True, default='', verbose_name='Виджет с картой точки')
    images = models.ImageField
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edit_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')

    def publish(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title