from django.db import models


class AdCategory(models.TextChoices):
    car = 'c', 'CAR'
    motorcycle = 'mc', 'MOTORCYCLE'
    bicycle = 'bc', 'BICYCLE'
