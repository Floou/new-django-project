from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Trainer

class TrainerBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def to_html(self):
        return f'<i>{self.added.strftime("%Y.%m.%d %H:%M")}</i>: <b>{self.trainer.name}</b>'
