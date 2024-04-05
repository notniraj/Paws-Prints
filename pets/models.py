from django.db import models
from users.models import UserModel

# Create your models here.
class PetModel(models.Model):
    
    pet_name = models.CharField(max_length=50, blank=False,null=False)
    pet_type = models.CharField(max_length=50, blank=False,null=False)
    pet_breed = models.CharField(max_length=50, blank=False,null=False)
    pet_profile = models.ImageField(upload_to="images/")
    pet_color = models.CharField(max_length=40, blank=True, null=True)
    pet_description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=None)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'pet_name'], name="unique_owner_pet")
        ]
        
    def __str__(self):
        return f"{self.owner} : {self.pet_name}"
    