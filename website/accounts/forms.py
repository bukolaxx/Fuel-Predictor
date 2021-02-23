from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
                "username",
                "password1", 
                "password2", 
            )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile

        fields = (
            'Full_Name',
            'Address1', 
            'Address2', 
            'City', 
            'State',
            'Zipcode'
        )