# Generated by Django 2.0.7 on 2018-07-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_auto_20180709_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=models.ManyToManyField(blank=True, to='movieapp.Comment'),
        ),
    ]
