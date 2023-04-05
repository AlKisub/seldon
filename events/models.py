from django.conf import settings
from django.db import models
from django.utils import timezone


class Events(models.Model):
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    edit_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')

    def publish(self):
        self.edit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject
