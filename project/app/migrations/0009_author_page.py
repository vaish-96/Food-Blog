# Generated by Django 2.2.5 on 2020-02-13 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200206_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Items')),
            ],
        ),
    ]