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
    time = models.TimeField(default='10:00')
    visitors = models.IntegerField()
    table = models.IntegerField(default=1)
    restaurant = models.ForeignKey(
        Restaurant,
        models.CASCADE,
        related_name='reservations'
    )
