# forms.py
from django import forms
from .models import Data

class PantryForm(forms.ModelForm):
    class Meta:
        model = Data
        fields =['item_name', 'quantity', 'Manufacturing_date', 'Expiration_date']


