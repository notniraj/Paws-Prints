from django.contrib.auth.forms import forms
from .models import PetModel

class PetRegistration(forms.Form):
    
    class Meta:
        model = PetModel
        fields = [
            'pet_picture',
            'pet_name',
            'pet_type',
            'pet_breed',
            'pet_color',
            'pet_description'
            'owner'
            ]