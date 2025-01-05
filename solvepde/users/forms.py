from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {'username', 'password1', 'password2'}


# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = {'username', 'password'}


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
