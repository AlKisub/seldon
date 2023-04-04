from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewsForm
from .models import News
from seldon.settings import MEDIA_ROOT


def news_list(request):
    news_list = News.objects.all()
    print(news_list)
    if not news_list:
        news_list = []
    return render(request, 'news/news_list.html', {'news_list': news_list})


@login_required(login_url='login')
def news_edit(request):
    pass


@login_required(login_url='login')
def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_create.html', {'form': form})
