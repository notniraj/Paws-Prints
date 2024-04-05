from django.shortcuts import render, redirect
from .forms import PetRegistration
# Create your views here.

def index(request):
    return render(request, "pets/index.html")


def add_pet(request):
    if request.method == 'GET':
        form = PetRegistration()
    else:
        form = PetRegistration(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pets:index")
    return render(request, 'pets/add-pet.html', {'form':form})