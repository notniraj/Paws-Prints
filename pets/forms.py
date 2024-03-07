from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import PetModel

class PetRegistration(ModelForm):
    
    class Meta:
        model = PetModel
        fields = '__all__'