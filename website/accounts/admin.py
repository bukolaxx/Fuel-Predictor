from django.contrib import admin
from .models import UserProfile, UserFuelForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import User

# Register your models here.
admin.site.register(UserProfile)