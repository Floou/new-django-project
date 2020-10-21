# Generated by Django 2.2 on 2020-10-21 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20201022_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rival', models.CharField(max_length=128)),
                ('result_match', models.IntegerField(default=0)),
                ('broadcast', models.IntegerField(default=0)),
                ('interceptions', models.IntegerField(default=0)),
                ('tool', models.IntegerField(default=0)),
                ('block_shot', models.IntegerField(default=0)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Team')),
            ],
        ),
        migrations.CreateModel(
            name='LineUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('patronymic', models.CharField(max_length=128)),
                ('number', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=128)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Trainer')),
            ],
        ),
    ]
