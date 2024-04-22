from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .models import Review, UserModel
from pets.models import PetModel
from .forms import ReviewForm, RegistrationForm, EditProfileForm
from pets.forms import PetRegistration
from star_ratings.models import Rating


# Create your views heres.
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
    edit_form = EditProfileForm(request.POST or None, request.FILES or None, instance=user, initial={'username': user.username})

    if request.method == 'POST':
        pet_form = PetRegistration(request.POST, request.FILES, user=user)  # Pass the user to initialize the owner field
        if 'edit_profile' in request.POST:
            edit_form = EditProfileForm(request.POST, request.FILES, instance=user)
            if edit_form.is_valid():
                edited_user = edit_form.save(commit=False)
                if 'profile_picture' in request.FILES:
                    edited_user.profile_picture = request.FILES['profile_picture']  # Update profile picture
                edited_user.save()  # Save the edited user profile information
                return redirect('users:user-profile')
            else:
                print(edit_form.errors)  # Print form errors for debugging
        elif 'delete_profile' in request.POST:
            user.delete()
            return redirect('users:logout')
        elif 'delete_pet' in request.POST:
            pet_id = request.POST.get('delete_pet')
            pet = get_object_or_404(PetModel, id=pet_id)
            pet.delete()
            return redirect('users:user-profile')
        elif 'edit_pet' in request.POST:
            pet_id = request.POST.get('edit_pet')
            pet_instance = get_object_or_404(PetModel, id=pet_id)  # Retrieve the pet instance
            pet_form = PetRegistration(request.POST or None, instance=pet_instance)  # Initialize the form with the instance
            if pet_form.is_valid():
                pet_form.save(commit=False)
                pet_form.owner = request.user
                pet_form.save()
                return redirect('users:user-profile')
            else:
                print(pet_form.errors)
        elif pet_form.is_valid():
            pet = pet_form.save(commit=False)
            pet.owner = user
            pet.save()
            return redirect('users:user-profile')

    else:   
        print("POST Data:", request.POST)
        pet_id = request.POST.get('edit_pet')
        print("Pet ID from POST data:", pet_id)  # Print pet_id to check its value
        pet_form = PetRegistration(user=user)  # Pass the user to initialize the owner field
        # Exclude the owner field from the form
        pet_form.fields['owner'].widget = forms.HiddenInput()

    context = {
        'user': user,
        'edit_form': edit_form,
        'pet_form': pet_form
    }
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='users:login')
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('users:reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
        'form': form
    }
    return render(request, 'users/reviews.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Updating session to avoid user log out after password change
            update_session_auth_hash(request, user)
            return redirect('users:user-profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change-password.html', {'form': form})


