from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)

    price = models.FloatField()
    color = models.CharField


