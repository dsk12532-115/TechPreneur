# Generated by Django 2.2.1 on 2019-09-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0011_auto_20190911_1119'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Give',
        ),
        migrations.AddField(
            model_name='vacant_seats',
            name='vacant_time',
            field=models.IntegerField(default=0, verbose_name='待ち時間'),
        ),
    ]