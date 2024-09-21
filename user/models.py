from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    identity_number = models.CharField(max_length=50,unique=True,)
    name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username}"
