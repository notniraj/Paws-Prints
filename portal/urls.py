from django.urls import path

from . import views

app_name = "portal"
urlpatterns = [
    path("", views.index, name ="index"),
    path("listing", views.listings, name="listing"),
    path("add-listing",views.add_listing, name="add-listing"),
    path('<int:listing_id>/map/', views.listing_map, name='listing-map'),
    path('listing/<int:listing_id>/', views.add_comment, name='view-comment'),
]
