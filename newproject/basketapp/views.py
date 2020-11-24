from basketapp.models import TrainerBasket
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from mainapp.models import Trainer

@login_required
def index(request):
    items = TrainerBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)

@login_required
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

@login_required
def remove(request, tr):
    if request.is_ajax():
        item = TrainerBasket.objects.get(id=tr)
        item.delete()
        return JsonResponse({'status': 'ok',
                             'tr': tr})
