# Generated by Django 3.2.7 on 2021-10-07 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appTeamGym', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='plan',
        ),
    ]