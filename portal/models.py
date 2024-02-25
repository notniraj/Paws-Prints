from django.db import models
from users.models import UserModel

from pets.models import PetModel

# Create your models here.
class Listings(models.Model):

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_lost = models.DateField(null=False)
    date_found = models.DateField(null=False)
    is_found = models.BooleanField(default=True)
    pet_id = models.ForeignKey(PetModel, on_delete=models.CASCADE, default=None)

