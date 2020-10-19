from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def news(request):
    return render(request, 'mainapp/news.html')


def registration(request):
    return render(request, 'mainapp/registration.html')