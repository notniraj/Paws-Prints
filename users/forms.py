from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel, ReviewsModel
from django.forms import ModelForm

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

class EditProfileForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True  # Making sure username field is disabled

    def clean_username(self):
        return self.instance.username  # Ensure no changes are made to the username

    class Meta:
        model = UserModel
        fields = ['profile_picture', 'username', 'email', 'password', 'user_type', 'first_name', 'last_name', 'address', 'contact', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'type': 'date'})
        }

class ReviewsForm(ModelForm):
    
    class Meta:
        model = ReviewsModel
        fields = '__all__'
        
        widgets = {
            
        }
        


    
        