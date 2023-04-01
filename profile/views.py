from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def account_page(request):
    print(request)
    login = request.user
    return render(request, 'profile/profile.html', {'login': login})

