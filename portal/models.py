from django.db import models
from users.models import UserModel
from django.utils import timezone

from django.conf import settings
from pets.models import PetModel

# Listings Model
class Listings(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_lost = models.DateField(null=False)
    date_found = models.DateField(null=True, blank=True)
    pet = models.ForeignKey(PetModel, on_delete=models.CASCADE)
    more_info = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.pet} : Lost: {self.date_lost}" if self.date_found  == None else f"{self.user_id} : {self.pet} : Found Date: {self.date_found}"

# Listing Comments Model
class ListingComments(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(null=True, blank=True)
    downvotes = models.IntegerField(null=True, blank=True)


# Pet Care Tip Model (Future Work)
class PetCareTip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(UserModel, related_name='petcaretips', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    tip = models.ForeignKey(PetCareTip, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(UserModel, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]