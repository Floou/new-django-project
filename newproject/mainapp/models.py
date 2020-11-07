from django.db import models


class Team(models.Model):
    command = models.CharField('Команда', max_length=128)
    win = models.IntegerField('Победы', default=0)
    defeat = models.IntegerField('Поражения', default=0)

    def __str__(self):
        return self.command

    class Meta:
        verbose_name = 'Команды'
        verbose_name_plural = 'Команда'


class Trainer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=128)
    surname = models.CharField('Фамилия', max_length=128)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Тренеры'
        verbose_name_plural = 'Тренер'


class Match(models.Model):
    team_owner = models.ForeignKey(Team, related_name='team_1', on_delete=models.CASCADE)
    team_guest = models.ForeignKey('Team', related_name='team_2', on_delete=models.CASCADE)
    result_match = models.IntegerField('Результат матча', default=0)
    broadcast = models.IntegerField('Передачи', default=0)
    interceptions = models.IntegerField('Перехваты', default=0)
    rebounds = models.IntegerField('Подборы', default=0)
    block_shot = models.IntegerField('Блокшоты', default=0)
    win_owner = models.BooleanField('Победа хозяев', default=True)
    win_guest = models.BooleanField('Победа гостей', default=False)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.result_match)

    class Meta:
        verbose_name = 'Матчи'
        verbose_name_plural = 'Матч'


class Player(models.Model):
    name = models.CharField('Имя', max_length=128)
    surname = models.CharField('Фамилия', max_length=128)
    number = models.IntegerField('Номер', default=0)
    position = models.CharField('Позиция', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игроки'
        verbose_name_plural = 'Игрок'
