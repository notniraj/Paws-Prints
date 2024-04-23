from django.contrib.auth.forms import UserCreationForm
from .models import UserModel, Review

from django.contrib.auth.forms import forms
from django.core.exceptions import ValidationError



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
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'user_type', 'first_name', 'last_name', 'contact', 'profile_picture', 'date_of_birth', 'address']
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        # Exclude the 'username' field from the form's fields
        self.fields.pop('username', None)

    # Override clean method to exclude 'username' field from validation
    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['username'] = self.instance.username  # Set the username to the current user's username
        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS class to the rating field for styling
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
        
    # Handle form validation on wrong rating pass.
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise ValidationError("Rating must be between 1 and 5.")
        return rating


