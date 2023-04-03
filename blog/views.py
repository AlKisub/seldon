from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse

from seldon.settings import MEDIA_ROOT
from .models import Post, Point, Photo
from .forms import PostForm, PointForm


def post_list(request):
    posts = Post.objects.filter(edit_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, pk=post)
    points = Point.objects.filter(post=post).order_by('sequence_number')
    points = points if points else []
    for point in points:
        point.photo = Photo.objects.filter(point=point)
    return render(request, 'blog/post_detail.html', {'post': post, 'points': points})


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def point_new(request, post):
    if request.method == "POST":
        form = PointForm(request.POST)
        if form.is_valid():
            point = form.save(commit=False)
            point.author = request.user
            point.edit_date = timezone.now()
            point.save()
            for image in request.FILES.getlist('images'):
                photo = Photo.objects.create(
                    image=image,
                    point_id=point.id,
                )
                initial_path = photo.image.path
                photo.image.name = f'{point.id}/{photo.image.name}'
                new_path = Path(MEDIA_ROOT, photo.image.name)
                new_path.parent.mkdir(exist_ok=True, parents=True)
                Path(initial_path).rename(new_path)
                photo.save()
            return redirect('post_detail', post=post)
    else:
        sequence_number = 1
        points = Point.objects.filter(post=post).order_by('-sequence_number')
        if points:
            sequence_number = points[0].sequence_number + 1
        form = PointForm(initial={'post': post, 'sequence_number': sequence_number})
    return render(request, 'blog/point_new.html', {'form': form})


@login_required(login_url='login')
def point_edit(request, post, point):
    edit_point = get_object_or_404(Point, pk=point, post=post)
    if request.method == "POST":
        form = PointForm(request.POST, instance=edit_point)
        if form.is_valid():
            edit_point = form.save(commit=False)
            edit_point.author = request.user
            edit_point.edit_date = timezone.now()
            edit_point.save()
            for image in request.FILES.getlist('images'):
                photo = Photo.objects.create(
                    image=image,
                    point_id=point,
                )
                initial_path = photo.image.path
                photo.image.name = f'{point}/{photo.image.name}'
                new_path = Path(MEDIA_ROOT, photo.image.name)
                new_path.parent.mkdir(exist_ok=True, parents=True)
                Path(initial_path).rename(new_path)
                photo.save()
            return redirect('post_detail', post=post)
    else:
        form = PointForm(instance=edit_point)
        photos = Photo.objects.filter(point=point)
    return render(request, 'blog/point_edit.html', {'form': form, 'photos': photos})


@login_required(login_url='login')
def delete_media(request):
    path = request.GET.get('path')
    photo = Photo.objects.filter(image=path)

    Path(MEDIA_ROOT, path).unlink()

    photo.delete()
    return HttpResponse(status=200)
