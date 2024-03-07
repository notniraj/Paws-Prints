from django.urls import path

from . import views

app_name = "portal"
urlpatterns = [
    path("", views.index, name ="index"),
    path("lost-listing", views.listings, name="lost-listing"),
    path("add-listing",views.add_listing, name="add-listing"),
]
