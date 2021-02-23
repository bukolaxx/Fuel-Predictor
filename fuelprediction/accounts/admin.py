from django.contrib import admin
from .models import UserProfile,UserFuelForm
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserFuelForm)