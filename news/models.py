from django.conf import settings
from django.db import models


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return self.subject
