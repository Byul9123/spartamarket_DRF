from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return self.username
