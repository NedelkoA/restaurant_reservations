from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import time, date


class Restaurant(models.Model):
    title = models.CharField(max_length=64)
    number_tables = models.IntegerField(validators=[MinValueValidator(5)])

    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.title


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField(
        validators=[
            MinValueValidator(time(10, 00)),
            MaxValueValidator(time(20, 00))
        ])
    table = models.IntegerField()
    visitors = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ])
    contact_email = models.EmailField()
    restaurant = models.ForeignKey(
        Restaurant,
        models.CASCADE,
        related_name='reservations'
    )
