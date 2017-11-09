from django.db import models


class Customer(models.Model):
    date = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(max_length=200)