from django.conf import settings
from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    name = models.CharField(max_length=200, verbose_name='Имя')
    about_me = models.TextField(verbose_name='О себе')
    photo = models.ImageField(upload_to='profile/', blank=True, verbose_name='Фото')
    rule = models.CharField(max_length=200, verbose_name='Роль')

    def __str__(self):
        return self.name
