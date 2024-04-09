from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import ReviewsModel, UserModel
from pets.models import PetModel
from .forms import ReviewsForm, RegistrationForm, EditProfileForm
from pets.forms import PetRegistration

    
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "portal/index.html")

def login_view(request):
    if request.method == "POST":
        username  = request.POST["username"]
        password  = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the 'next' parameter exists in the request
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)  # Redirect to the URL specified in 'next'
            else:
                return HttpResponseRedirect(reverse("users:index"))  # Redirect to the default URLs
        else:
            if username == "" or password == "":
                return render(request, "users/login.html", {
                "message": "Please enter username and password!"
            })
            else:    
                return render(request, "users/login.html", {
                    "message": "Invalid credentials."
                })
    return render(request, "users/login.html")

def signup_view(request):   
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.password = make_password(form.cleaned_data['password1'])
            user.save()
            return render(request, "users/login.html", {
                "message" : "Registration Succesful."
            })  # Redirect to a login page
    return render(request, 'users/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Successfully Logged Out."
    })
    
UserModel = get_user_model()

@login_required(login_url='users:login')
def user_profile(request):
    user = request.user
    pet_form = PetRegistration(request.POST or None, request.FILES or None) 
    edit_form = EditProfileForm(request.POST or None, request.FILES or None, instance=user, initial={'username': user.username})
    
    if request.method == 'POST':
        if 'edit_profile' in request.POST:
            edit_form = EditProfileForm(request.POST, request.FILES, instance=user)
            if edit_form.is_valid():
                edited_user = edit_form.save(commit=False)
                edited_user.profile_picture = request.FILES.get('profile_picture')  # Update profile picture
                edited_user.save()  # Save the edited user profile information
                return redirect('users:user-profile')
            else:
                print(edit_form.errors)  # Print form errors for debugging
        elif 'delete_profile' in request.POST:
            user.delete()
            return redirect('users:logout')
        elif 'delete_pet' in request.POST:
            pet_id = request.POST.get('users:delete_pet')
            pet = get_object_or_404(PetModel, owner=user, id=pet_id)
            pet.delete()
            return redirect('user-profile')
        elif 'edit_pet' in request.POST:
            pet_id = request.POST.get('users:edit_pet')
            pet_instance = get_object_or_404(PetModel.objects.filter(owner=user), id=pet_id)
            pet_form = PetRegistration(request.POST, request.FILES, instance=pet_instance)
            if pet_form.is_valid():
                pet_form.save()
                return redirect('users:user-profile')
        elif pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.owner = user
            pet.save()
            return redirect('users:user-profile')
    else:
        # Exclude the owner field from the form
        pet_form.fields['owner'].widget = forms.HiddenInput()
    context = {
        'user': user,
        'edit_form': edit_form,
        'pet_form': pet_form
    }
    return render(request, 'users/user-profile.html', context)
    
    
def reviews(request):
    # reviews = ReviewsModel.objects.create(user_id, message, rating)
    # reviews.save()
    if request.method == 'GET':
        form = ReviewsForm()
    else:
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewsForm()
            return render(request, "users/reviews.html", {
                    "message" : "Review Posted. Thank you for supporting the community!",
                    "form" : form   
                })
    return render(request, 'users/reviews.html', {'form' : form})