import authapp.views as authapp
from django.urls import path
from django.contrib.auth.models import User

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
]
