# Generated by Django 2.2 on 2020-10-19 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_lastmatches_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastmatches',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
