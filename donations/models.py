from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import CustomUser

# Create your models here.

class FundraiseCause(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.IntegerField()
    current_amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    account_number = models.IntegerField(null=False, blank=False)
    image = models.ImageField( upload_to='cause_images', null=True, blank=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name  = 'causes')
                              
    def save (self, *args, **kwargs):
        if self.image is not None:
            self.image.name = 'cause_images/default.webp'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.IntegerField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    cause = models.ForeignKey(FundraiseCause, on_delete=models.CASCADE, related_name='donations')

    def __str__(self):
        return self.name
    