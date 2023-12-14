from django import forms
from .models import FundraiseCause, Donation

class FundraiseCauseForm(forms.ModelForm):
    class Meta:
        model = FundraiseCause
        fields =  ['title', 'description', 'goal', 'account_number',  'image'] 
        #current_amount is not included because it is automatically set and 
        #should not be set by the user

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount', 'phone_number']

        