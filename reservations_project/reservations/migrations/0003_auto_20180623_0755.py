# Generated by Django 2.0.6 on 2018-06-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20180622_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default='10:00'),
        ),
    ]
