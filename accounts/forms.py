from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')
        
    def __str__(self):
        return self.username
    
class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        
    def __str__(self):
        return self.username

