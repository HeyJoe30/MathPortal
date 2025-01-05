from django.urls import path
from . import views

app_name = 'users'

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('index/',  CongratulationsView.as_view(), name='index'),
# ]

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]

