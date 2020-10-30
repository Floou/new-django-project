# Generated by Django 2.2 on 2020-10-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Состав команды',
                'verbose_name_plural': 'Состав команд',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=128)),
                ('win', models.IntegerField(default=0)),
                ('defeat', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Команды',
                'verbose_name_plural': 'Команда',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Team')),
            ],
            options={
                'verbose_name': 'Тренеры',
                'verbose_name_plural': 'Тренер',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=128)),
                ('line_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.LineUp')),
            ],
            options={
                'verbose_name': 'Игроки',
                'verbose_name_plural': 'Игрок',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.CharField(max_length=128)),
                ('result_match', models.IntegerField(default=0)),
                ('broadcast', models.IntegerField(default=0)),
                ('interceptions', models.IntegerField(default=0)),
                ('tool', models.IntegerField(default=0)),
                ('block_shot', models.IntegerField(default=0)),
                ('win_owner', models.BooleanField(default=True)),
                ('win_guest', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
                ('team_guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match1', to='mainapp.Team')),
                ('team_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='mainapp.Team')),
            ],
            options={
                'verbose_name': 'Матчи',
                'verbose_name_plural': 'Матч',
            },
        ),
        migrations.AddField(
            model_name='lineup',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Match'),
        ),
    ]
