# Generated by Django 2.2 on 2020-10-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201019_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='composition',
            name='position',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]