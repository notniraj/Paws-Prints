from django.contrib import admin

from .models import UserModel
from .models import UserType
from .models import Review
# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "comment", "rating", "created_at")
    
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "role", "is_active")

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name", "contact", "address", "user_type")

admin.site.register(UserModel, UserAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Review, ReviewsAdmin)