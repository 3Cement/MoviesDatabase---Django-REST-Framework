# Generated by Django 2.0.7 on 2018-07-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('comment', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]