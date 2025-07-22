from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.ImageField()


class Reservation(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    comments = models.CharField(max_length=1000)
