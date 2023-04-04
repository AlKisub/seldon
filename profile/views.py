from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from profile.forms import ProfileForm
from profile.models import Profile
from seldon.settings import MEDIA_ROOT


@login_required(login_url='login')
def account_page(request):
    login = request.user
    if Profile.objects.filter(author=login):
        profile = Profile.objects.filter(author=login)[0]
        return render(request, 'profile/profile.html', {'login': login, 'profile': profile})
    else:
        Profile.objects.create(author=login)
        return redirect('account_edit')



@login_required(login_url='login')
def account_edit(request):
    profile = get_object_or_404(Profile, author=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            edit_profile = form.save(commit=False)
            # form = form.save(commit=False)
            # form.author = request.user
            # form.edit_date = timezone.now()
            edit_profile.save()
            return redirect('account_page')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/edit.html', {'form': form})


@login_required(login_url='login')
def change_password(request, error='', success=''):
    if request.method == 'POST':
        u = User.objects.get(username=request.user)
        if not check_password(request.POST.get('old_password'), u.password):
            error = 'Старый пароль введён не верно'
        elif request.POST.get('new_password1') != request.POST.get('new_password2'):
            error = 'Введённые пароли не совпадают'
        else:
            u.set_password(request.POST.get('new_password1'))
            u.save()
            success = 'Пароль успешно изменен'
    return render(request, 'profile/change_pass.html', {'error': error, 'success': success})


def account_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profile/profiles.html', {'profiles': profiles})
