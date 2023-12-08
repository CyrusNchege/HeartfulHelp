from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import FundraiseCause, Donation
from .forms import FundraiseCauseForm, DonationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'donations/about.html')

