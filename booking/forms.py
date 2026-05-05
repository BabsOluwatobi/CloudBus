from django import forms
from .models import BusPass

class BusPassForm(forms.ModelForm):
    class Meta:
        model = BusPass
        fields = ['source', 'destination', 'travel_date']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }