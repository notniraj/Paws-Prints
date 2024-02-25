from django.db import models
from users.models import UserModel

from pets.models import PetModel

# Create your models here.
class Listings(models.Model):

    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date_lost = models.DateField(null=False)
    date_found = models.DateField(null=True, blank=True)
    is_found = models.BooleanField(default=True)
    pet_id = models.ForeignKey(PetModel, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.pet_id} : Lost: {self.date_lost}" if self.date_found  == None else f"{self.user_id} : {self.pet_id} : Found Date: {self.date_found}"

