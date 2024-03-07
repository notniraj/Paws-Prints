from django.urls import path

from . import views

app_name = "pets"
urlpatterns = [
    path("", views.index, name ="index"),
    path("add-pet", views.add_pet, name="add-pet"),
]
