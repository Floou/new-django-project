# Generated by Django 2.2 on 2020-11-07 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201031_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name_team',
            new_name='command',
        ),
    ]
