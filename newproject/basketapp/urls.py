import basketapp.views as basketapp
from django.urls import path

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:trainer_id>/', basketapp.add, name='add'),
]