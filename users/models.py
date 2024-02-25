from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import AbstractUser

fs = FileSystemStorage(location="/media/photos")



# Create your models here.

class UserType(models.Model):
    role = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.role

    
class UserModel(AbstractUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=fs, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100)
    pet_picture = models.ImageField(upload_to=fs, default='img1')
    pet_name = models.CharField(max_length=30, blank=True, null=True)
    pet_type = models.CharField(max_length=30, blank=True, null=True)
    breed = models.CharField(max_length=30, blank=True, null=True )
    pet_color = models.CharField(max_length=40, blank=True, null=True)
    pet_description = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username