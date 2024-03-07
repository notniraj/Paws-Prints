from django.contrib.auth.forms import UserCreationForm
from .models import UserModel

from django.contrib.auth.forms import forms

class RegistrationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = [
            'profile_picture',
            'username',
            'email',
            'password1',
            'password2',
            'user_type',
            'first_name',
            'last_name',
            'address',
            'contact',
            'date_of_birth'
            ]
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'type': 'date'})
        }
        
        