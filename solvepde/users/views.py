from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.views import View
from .forms import RegisterForm, LoginForm


class CongratulationsView(View):
    def get(self, request):
        return render(request, 'users/index.html')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'regular'
            login(request, user)
            # return redirect('chat:chat_room')
            return render(request, 'users/index.html')
        return render(request, 'users/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # user = form.get_user()
            # if user is not None and user.is_active:
            #     login(request, form.get_user())
            # else:
            #     form.add_error(None, 'Ваш аккаунт заблокирован')
            # return redirect('chat:chat_room')
            return render(request, 'users/index.html')
        # return render(request, 'auth/login.html', {'form': form})
        return render(request, 'users/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')