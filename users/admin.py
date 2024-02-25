from django.contrib import admin

from .models import UserModel
from .models import UserType

# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserType)