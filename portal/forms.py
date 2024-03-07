from django.contrib.auth.forms import forms
from django.forms import ModelForm

from .models import Listings


class AddListingForm(ModelForm):
    
    class Meta:
        model = Listings
        fields = '__all__'