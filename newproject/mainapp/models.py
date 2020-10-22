from django.db import models


class Team(models.Model):
    name_team = models.CharField(max_length=128)
    win = models.IntegerField(default=0)
    defeat = models.IntegerField(default=0)

    def __str__(self):
        return self.name_team

    class Meta:
        verbose_name = 'Команды'
        verbose_name_plural = 'Команда'


class Trainer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Тренеры'
        verbose_name_plural = 'Тренер'


class LineUp(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    position = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состав команды'
        verbose_name_plural = 'Состав команд'


class Match(models.Model):
    owner = models.ForeignKey(Team, on_delete=models.CASCADE)
    guest = models.CharField(max_length=128)
    result_match = models.IntegerField(default=0)
    broadcast = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    tool = models.IntegerField(default=0)
    block_shot = models.IntegerField(default=0)
    win_owner = models.BooleanField(default=True)
    win_guest = models.BooleanField(default=True)

    def __str__(self):
        return str(self.result_match)

    class Meta:
        verbose_name = 'Матчи'
        verbose_name_plural = 'Матч'
