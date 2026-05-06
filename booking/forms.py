from django import forms
from .models import BusPass
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --- 1. THE BOOKING FORM ---
class BusPassForm(forms.ModelForm):
    class Meta:
        model = BusPass
        fields = ['source', 'destination', 'travel_date']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }

# --- 2. THE REGISTRATION FORM ---
# Make sure this name matches exactly what is in views.py
class EnhancedRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)