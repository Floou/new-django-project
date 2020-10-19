from django.db import models


class Command(models.Model):
    command = models.CharField(max_length=128)
    win = models.IntegerField(default=0)
    defeat = models.IntegerField(default=0)

    def __str__(self):
        return self.command


class Composition(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    command = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Match(models.Model):
    command = models.CharField(max_length=128)
    rebounds = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    transmission = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def __str__(self):
        return self.command