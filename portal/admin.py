from django.contrib import admin

from .models import Listings,  ListingComments

# Register your models here.
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "pet_id", "date_lost", "date_found", "is_found")
    
class ListingCommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "comment", "last_seen_location")

admin.site.register(Listings, ListingsAdmin)
admin.site.register(ListingComments, ListingCommentsAdmin)