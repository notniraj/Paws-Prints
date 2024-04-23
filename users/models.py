from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q

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
    profile_picture = models.ImageField(upload_to="images/", blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Review(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    