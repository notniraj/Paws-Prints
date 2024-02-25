from django.contrib import admin

from .models import Listings

# Register your models here.
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "pet_id", "date_lost", "date_found", "is_found")

admin.site.register(Listings, ListingsAdmin)