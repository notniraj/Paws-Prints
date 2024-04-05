from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms 

from .forms import AddListingForm
from .models import Listings

# Create your views here.
def index(request):
    return render(request, "portal/index.html")

def listings(request):
    action = request.GET.get('action', None)
    if action == 'lost':
        if request.method == 'GET':
            form = AddListingForm()
        else:
            form = AddListingForm(request.POST)
            if form.is_valid():
                form.save()
                form = AddListingForm()
                lost_data = Listings.objects.filter(date_found__isnull=True)
            return render(request, "portal/lostlisting.html", {
                    "message" : "Listing Added.",
                    'lost_data' : lost_data,
                    'form': form
                })
        lost_data = Listings.objects.filter(date_found__isnull=True)
        lost_context = {
            'lost_data' : lost_data,
            'form': form
        }
        return render(request, "portal/lostlisting.html", lost_context)
    else:
        found_data = Listings.objects.filter(date_found__isnull=False)
        found_context = {
            'found_data' : found_data
        }
        return render(request, "portal/foundlisting.html", found_context)

def add_listing(request):
    if request.method == 'GET':
        form = AddListingForm()
    else:
        form = AddListingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("listing", {
                "message" : "Listing Added."
            })
    return render(request, 'portal/add-listing.html', {'form': form})

