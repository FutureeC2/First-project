from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    error_message = {
        'invalid_login': 'Неверный логин или пароль. Попробуйте еще раз!'
    }