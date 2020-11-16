from django.shortcuts import render

from mainapp.models import Team, Trainer, Match, Player


def index(request):
    return render(request, 'mainapp/index.html')


def commands(request):
    command = Team.objects.all()
    context = {
        'command': command,
        'page_title': 'Команды'
    }

    return render(request, 'mainapp/commands.html', context)


def commands_page(request, pk):
    team = Trainer.objects.filter(team_id=pk)
    context = {
        'team': team,
        'page_title': 'Тренер'
    }
    return render(request, 'mainapp/commands_page.html', context)


def trainer_page(request, pk):
    trainer = Trainer.objects.get(pk=pk)
    context = {
        'trainer': trainer,
        'page_title': 'Информация о тренере'
    }
    return render(request, 'mainapp/trainer_page.html', context)