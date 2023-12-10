from django.contrib import admin

# Register your models here.
from .models import FundraiseCause, Donation

admin.site.register(FundraiseCause)
admin.site.register(Donation)
