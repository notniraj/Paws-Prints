from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms 

from .forms import AddListingForm
from .models import Listings, ListingComments

from django.contrib.auth.decorators import login_required

@login_required
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


def add_comment(request, listing_id):
    if request.method == 'POST':
        user_id = request.user
        comment_text = request.POST.get('comment')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        listing_instance = Listings.objects.get(pk=listing_id)
        ListingComments.objects.create(user_id=user_id, listing_id=listing_instance, comment=comment_text, latitude=latitude, longitude=longitude)
        return redirect('portal:view-comment', listing_id=listing_id)
    else:
        listing = Listings.objects.filter(id=listing_id)
        comments = ListingComments.objects.filter(listing_id=listing_id)
        
        context = {
            'comments': comments,
            'listing': listing,
        }
        return render(request, 'portal/comment.html', context)

def listing_map(request, listing_id):
    # Fetch comments associated with the specific listing_id
    comments = ListingComments.objects.filter(listing_id=listing_id)

    # Pass comments data to the template context
    context = {
        'comments': comments,
        'listing_id': listing_id,
    }

    return render(request, 'portal/listing-map.html', context)

