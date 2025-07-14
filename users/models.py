from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        editable=False,
    )
    last_name = models.CharField(
        max_length=50,
        editable=False,
    )
    avatar = (
        models.ImageField(
            blank=True,
        ),
    )
    name = models.CharField(
        max_length=100,
    )
