from django.contrib.auth.forms import forms
from django.forms import ModelForm

from .models import Listings


class AddListingForm(ModelForm):
    
    class Meta:
        model = Listings
        fields = '__all__'
        
        
        widgets = {
            'date_found': forms.TextInput(attrs={'type': 'date'}),
            'date_lost': forms.TextInput(attrs={'type': 'date'})
        }

class SearchForm(ModelForm):
    
    class Meta:
        model = Listings
        fields = ['id']