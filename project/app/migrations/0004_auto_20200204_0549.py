# Generated by Django 2.2.5 on 2020-02-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200204_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='Profile_pic'),
        ),
        migrations.AlterField(
            model_name='items',
            name='food_image',
            field=models.ImageField(blank=True, upload_to='food_pic'),
        ),
    ]