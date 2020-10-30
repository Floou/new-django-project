from django.shortcuts import render

from mainapp.models import Team, Trainer, Match, Player


def index(request):
    return render(request, 'mainapp/index.html')


def news(request):
    name_team = Team.objects.all()
    context = {
        'name_team': name_team,
        'page_title': 'Новости'
    }

    return render(request, 'mainapp/news.html', context)


def registration(request):
    return render(request, 'mainapp/registration.html')


def news_page(request, pk):
    team = Team.objects.filter(team_id=pk)
    context = {
        'team': team,
        'page_title': 'Страница команд'
    }
    return render(request, 'mainapp/news_page.html', context)
