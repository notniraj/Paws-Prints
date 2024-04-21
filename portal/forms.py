from django.contrib.auth.forms import forms
from django.forms import ModelForm

from .models import Listings
from .models import PetCareTip, Comment


class AddListingForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddListingForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = user.petmodel_set.all()
    
    class Meta:
        model = Listings
        fields = ['date_lost', 'date_found', 'pet', 'more_info']
        widgets = {
            'date_found': forms.TextInput(attrs={'type': 'date'}),
            'date_lost': forms.TextInput(attrs={'type': 'date'})
        }

class SearchForm(ModelForm):
    
    class Meta:
        model = Listings
        fields = ['id']



class PetCareTipForm(forms.ModelForm):
    class Meta:
        model = PetCareTip
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']