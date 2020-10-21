from django.db import models


class Team(models.Model):
    name_team = models.CharField(max_length=128)
    win = models.IntegerField(default=0)
    defeat = models.IntegerField(default=0)

    def __str__(self):
        return self.name_team


class Trainer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return self.surname


class LineUp(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    number = models.IntegerField(default=0)
    position = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Match(models.Model):
    command = models.ForeignKey(Team, on_delete=models.CASCADE)
    rival = models.CharField(max_length=128)
    result_match = models.IntegerField(default=0)
    broadcast = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    tool = models.IntegerField(default=0)
    block_shot = models.IntegerField(default=0)

    def __str__(self):
        return self.command
