from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms 

from .forms import AddListingForm

# Create your views here.
def index(request):
    return render(request, "portal/index.html")

def listings(request):
    return render(render, "portal/lostlistings.html", {  
})
    
def add_listing(request):
    if request.method == 'GET':
        form = AddListingForm()
    else:
        form = AddListingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("lost-listing", {
                "message" : "Listing Added."
            })
    return render(request, 'portal/add-listing.html', {'form': form})