from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q

from .forms import AddListingForm
from .models import Listings, ListingComments

from django.contrib.auth.decorators import login_required
from .models import PetCareTip
from .forms import PetCareTipForm, CommentForm


@login_required(login_url='users:login')
def index(request):
    if request.method == 'GET': 
        recent_lost_listings = Listings.objects.filter(date_found__isnull=True).order_by('-date_lost')[:5]
    return render(request, "portal/index.html", {'recent_lost_listings': recent_lost_listings})

@login_required(login_url='users:login')
def listings(request):
    action = request.GET.get('action', None)
    user = request.user
    if action == 'lost':
        if request.method == 'GET':
            form = AddListingForm(user=user)
        else:
            form = AddListingForm(request.POST)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.user_id = user
                listing.save()
                form = AddListingForm(user = request.user)
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

@login_required(login_url='users:login')
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

@login_required(login_url='users:login')
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
    
@login_required(login_url='users:login')
def listing_map(request, listing_id):
    # Fetch comments associated with the specific listing_id
    comments = ListingComments.objects.filter(listing_id=listing_id)

    # Pass comments data to the template context
    context = {
        'comments': comments,
        'listing_id': listing_id,
    }

    return render(request, 'portal/listing-map.html', context)


@login_required(login_url='users:login')
def search_listing(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query').strip()
        if query:
            # Perform search query on listings
            search_results = Listings.objects.filter(pet__pet_name__icontains=query)
            results = [{'id': listing.id, 'owner': listing.user_id.username, 'pet_name': listing.pet.pet_name} for listing in search_results]
            return JsonResponse(results, safe=False)
    # If no results found or other error occurs, return an empty list as JSON
    return JsonResponse([], safe=False)


@login_required(login_url='users:login')
def petcare(request):
    return render(request, 'portal/careandtips.html')


@login_required(login_url='users:login')
def pet_care_tips(request):
    tips = PetCareTip.objects.all()
    tip_form = PetCareTipForm()
    comment_form = CommentForm()
    return render(request, "users/pet_care_tips.html", {'tips': tips, 'tip_form': tip_form, 'comment_form': comment_form})

@login_required(login_url='users:login')
def add_pet_care_tip(request):
    if request.method == 'POST':
        form = PetCareTipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            return redirect('pet_care_tips')
    else:
        form = PetCareTipForm()
    return render(request, 'users/add_pet_care_tip.html', {'form': form})
