from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import TrainerBasket
from django.urls import reverse

from mainapp.models import Trainer


def index(request):
    items = TrainerBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)


def add(request, trainer_id):
    trainer = Trainer.objects.get(pk=trainer_id)
    TrainerBasket.objects.get_or_create(
        user=request.user,
        trainer=trainer
    )
    return HttpResponseRedirect(
        reverse('mainapp:trainer_page',
                kwargs={'pk': trainer.pk})
    )


def remove(request, tr):
    item = TrainerBasket.objects.get(id=tr)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
