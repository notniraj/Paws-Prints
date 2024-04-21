from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import PetModel

class PetRegistration(ModelForm):
    
    class Meta:
        model = PetModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop the 'user' argument if it exists
        super(PetRegistration, self).__init__(*args, **kwargs)
        
        # Hide the owner field
        self.fields['owner'].widget = forms.HiddenInput()
        
        # Set the initial value of the owner field to the current user
        if user:
            self.fields['owner'].initial = user

    # Override the clean method to ensure the owner field is properly populated
    def clean(self):
        cleaned_data = super().clean()
        
        # If owner field is empty, set it to the initial value
        if 'owner' not in cleaned_data:
            cleaned_data['owner'] = self.initial.get('owner')
        return cleaned_data