# Generated by Django 2.2.5 on 2020-02-19 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='user_name',
        ),
    ]
