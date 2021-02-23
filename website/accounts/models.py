from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal

# Create your models here.
class UserProfile(models.Model):
    US_STATES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'),
    ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
        ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
        ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
        ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
        ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
        ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
        ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
        ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
        ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
        ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE,
    )
    Full_Name =models.CharField(max_length=50, default='', blank = False)
    Address1 = models.CharField(max_length=100, default='', blank=False)
    Address2 = models.CharField(max_length=100, default='', blank= True)
    City = models.CharField(max_length=100, default='', blank = False)
    State = models.CharField(max_length=5, choices=US_STATES, blank=False)
    Zipcode = models.CharField(max_length=9, blank=False, default='')

    def __str__(self):
        return str(self.user)

@receiver(post_save,sender=User)
def create_profile(sender, instance,created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)

    instance.profile.save()

post_save.connect(create_profile, sender= User)
