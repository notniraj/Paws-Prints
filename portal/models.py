from django.db import models
from users.models import UserModel
from django.utils import timezone

from django.conf import settings
from pets.models import PetModel

# Create your models here.
class Listings(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_lost = models.DateField(null=False)
    date_found = models.DateField(null=True, blank=True)
    pet_id = models.ForeignKey(PetModel, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.pet_id} : Lost: {self.date_lost}" if self.date_found  == None else f"{self.user_id} : {self.pet_id} : Found Date: {self.date_found}"


class ListingComments(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)