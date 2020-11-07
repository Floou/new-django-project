import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('commands/', mainapp.commands, name='commands'),
    path('commands/team/<int:pk>', mainapp.commands_page, name='commands_page'),
    path('commands/trainer/<int:pk>', mainapp.trainer_page, name='trainer_page'),
    path('basket/', mainapp.basket),
]