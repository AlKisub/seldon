from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required(login_url='login')
def account_page(request):
    print(request)
    login = request.user
    return render(request, 'profile/profile.html', {'login': login})


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
