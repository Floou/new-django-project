from django.shortcuts import render

from mainapp.models import Team, Trainer, Match, Player


def index(request):
    return render(request, 'mainapp/index.html')


def commands(request):
    name_team = Team.objects.all()
    context = {
        'name_team': name_team,
        'page_title': 'Команды'
    }

    return render(request, 'mainapp/commands.html', context)


def registration(request):
    context = {
        'page_title': 'Регистрация'
    }
    return render(request, 'mainapp/registration.html', context)


def commands_page(request, pk):
    team = Trainer.objects.filter(team_id=pk)
    context = {
        'team': team,
        'page_title': 'Тренер'
    }
    return render(request, 'mainapp/commands_page.html', context)

