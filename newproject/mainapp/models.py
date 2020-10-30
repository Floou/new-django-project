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


class Match(models.Model):
    team_owner = models.ForeignKey(Team, related_name='match', on_delete=models.CASCADE)
    team_guest = models.ForeignKey('Team', related_name='match1', on_delete=models.CASCADE)
    result_match = models.IntegerField(default=0)
    broadcast = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    tool = models.IntegerField(default=0)
    block_shot = models.IntegerField(default=0)
    win_owner = models.BooleanField(default=True)
    win_guest = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.result_match)

    class Meta:
        verbose_name = 'Матчи'
        verbose_name_plural = 'Матч'


class Player(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    position = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игроки'
        verbose_name_plural = 'Игрок'
