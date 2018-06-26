# Generated by Django 2.0.6 on 2018-06-26 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_auto_20180626_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='visitors',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
