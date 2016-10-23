from __future__ import unicode_literals
from django.db import models


class Deals(models.Model):
    name = models.TextField()
    image = models.ImageField()
    rating = models.FloatField()
    link = models.TextField()
    actual_price = models.FloatField()
    discount = models.IntegerField()
    location = models.TextField()