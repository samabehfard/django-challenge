from django.db import models
from django.contrib.auth.models import AbstractUser


class Stadium(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seat(models.Model):
    code = models.CharField(max_length=10)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.code} in {self.stadium}"


