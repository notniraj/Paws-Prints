from django.urls import path

from . import views

app_name = "portal"
urlpatterns = [
    path("", views.index, name ="index"),
    path("listing", views.listings, name="listing"),
    path("add-listing",views.add_listing, name="add-listing"),
]
