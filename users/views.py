from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms 
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password

from .models import ReviewsModel
from .forms import ReviewsForm
    
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
            return HttpResponseRedirect(reverse("users:index"))
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
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password1'])
            user.save()
            return redirect("", {
                "message" : "Registration Succesful."
            })  # Redirect to a login page
    return render(request, 'users/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Successfully Logged Out."
    })
    
    
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