from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import Role, User
from django.contrib.auth import login, logout, authenticate

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else: 
        form = RegisterForm()
    return render(request, 'register.html', {'form: form'})

def login_view(request):
    form = LoginForm(data = request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')