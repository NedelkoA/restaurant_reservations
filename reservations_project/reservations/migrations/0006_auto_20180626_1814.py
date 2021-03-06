# Generated by Django 2.0.6 on 2018-06-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_reservation_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='number_seats',
            new_name='number_tables',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='contact_email',
            field=models.EmailField(max_length=254),
        ),
    ]
