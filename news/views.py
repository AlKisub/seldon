from pytz import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewsForm
from .models import News
from seldon.settings import TIME_ZONE


def news_list(request):
    news_list = News.objects.all().order_by('-date')
    return render(request, 'news/news_list.html', {'news_list': news_list})


@login_required(login_url='login')
def news_edit(request, news):
    edit_news = get_object_or_404(News, pk=news)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=edit_news)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.save()
            return redirect('news_list')
    else:
        edit_news.date = edit_news.date.astimezone(timezone(TIME_ZONE)).isoformat()[:-6]
        form = NewsForm(instance=edit_news)
    return render(request, 'news/news_edit.html', {'form': form})


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
