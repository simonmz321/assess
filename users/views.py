from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def login_system(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['is_login'] = 'success'
            request.session['username'] = username
            return redirect('/home/')
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'users/login.html', {'error': error_msg})