from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone
from .models import Post, Point
from .forms import PostForm, PointForm


def post_list(request):
    posts = Post.objects.filter(edit_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, pk=post)
    points = Point.objects.filter(post=post).order_by('sequence_number')
    return render(request, 'blog/post_detail.html', {'post': post, 'points': points if points else []})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.edit_date = timezone.now()
            post.save()
            return redirect('post_detail', post=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, post):
    edit_post = get_object_or_404(Post, pk=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=edit_post)
        if form.is_valid():
            edit_post = form.save(commit=False)
            edit_post.author = request.user
            edit_post.edit_date = timezone.now()
            edit_post.save()
            return redirect('post_detail', post=post)
    else:
        form = PostForm(instance=edit_post)
    return render(request, 'blog/post_edit.html', {'form': form})


def point_new(request, post):
    if request.method == "POST":
        form = PointForm(request.POST)
        if form.is_valid():
            point = form.save(commit=False)
            point.author = request.user
            point.edit_date = timezone.now()
            point.save()
            return redirect('post_detail', post=post)
    else:
        sequence_number = 1
        points = Point.objects.filter(post=post).order_by('-sequence_number')
        if points:
            sequence_number = points[0].sequence_number + 1
        form = PointForm(initial={'post': post, 'sequence_number': sequence_number})
    return render(request, 'blog/point_new.html', {'form': form})


def point_edit(request, post, point):
    edit_point = get_object_or_404(Point, pk=point, post=post)
    if request.method == "POST":
        form = PointForm(request.POST, instance=edit_point)
        if form.is_valid():
            edit_point = form.save(commit=False)
            edit_point.author = request.user
            edit_point.edit_date = timezone.now()
            edit_point.save()
            return redirect('post_detail', post=post)
    else:
        form = PointForm(instance=edit_point)
    return render(request, 'blog/point_edit.html', {'form': form})
