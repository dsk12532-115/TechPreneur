# Generated by Django 2.2.1 on 2019-09-11 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0009_auto_20190910_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='give_point',
            field=models.IntegerField(default=0, verbose_name='ゆずりポイント'),
        ),
        migrations.AddField(
            model_name='profile',
            name='given_point',
            field=models.IntegerField(default=0, verbose_name='ゆずられポイント'),
        ),
    ]
