from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True) 
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    

    def __str__(self):
        return self.username
