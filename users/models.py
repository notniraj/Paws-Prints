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
    
class ReviewsModel(models.Model):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=0)
    review_message = models.TextField(blank=True)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0),]
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(rating__gte=0.0) & Q(rating__lte=5.0),
                name='reviews_ratings_range'),
            )
        
    def __str__(self):
        return f"{self.user_id.username} : {self.rating}"
    