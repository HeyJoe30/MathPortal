from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

# app_name = 'users'

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('index/',  CongratulationsView.as_view(), name='index'),
# ]

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
]

