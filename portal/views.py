from django.shortcuts import render
from django.http import HttpResponse
from django import forms 

# Create your views here.
def index(request):
    return render(request, "portal/index.html")

def listings(request):
    return render(render, "portal/listings.html", {
        
    })
