from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=64)
    number_seats = models.IntegerField()

    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.title


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField(default='00:00')
    visitors = models.IntegerField()
    restaurant = models.ForeignKey(
        Restaurant,
        models.CASCADE,
        related_name='reservations'
    )
