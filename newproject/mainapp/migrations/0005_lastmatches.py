# Generated by Django 2.2 on 2020-10-19 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20201019_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastMatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=128)),
                ('result', models.CharField(max_length=128)),
                ('rebounds', models.IntegerField(default=0)),
                ('interceptions', models.IntegerField(default=0)),
                ('transmission', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
            ],
        ),
    ]
