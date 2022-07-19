from django.db import models

# Create your models here.

class Owner(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Vehicle(models.Model):
    username = models.ForeignKey(Owner, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    license = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)

    def __str__(self):
        return self.make