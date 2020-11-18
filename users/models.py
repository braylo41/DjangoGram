from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=30)
    state = models.CharField(null=True, blank=True, max_length=30)
