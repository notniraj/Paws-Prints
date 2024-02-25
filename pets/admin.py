from django.contrib import admin

from .models import PetModel

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "pet_name",
        "pet_type",
        "pet_breed",
        "pet_color",
        )

admin.site.register(PetModel, PetAdmin)