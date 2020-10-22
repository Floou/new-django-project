from django.shortcuts import render

from mainapp.models import Team

def index(request):
    return render(request, 'mainapp/index.html')


def news(request):
    name_team = Team.objects.all()
    context = {
        'name_team': name_team
    }

    return render(request, 'mainapp/news.html', context)


def registration(request):
    return render(request, 'mainapp/registration.html')