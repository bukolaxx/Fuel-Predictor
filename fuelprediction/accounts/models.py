from django.db import models
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
        # null=True,
        # related_name='profile',
        # verbose_name="related user",
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

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender= User)

class UserFuelForm(models.Model):
    # user.userprofile
    # user = models.OneToOneField(User,null=True,related_name = 'profile', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField('Gallons Requested', default=1)
    deliveryAddress = models.CharField('Delivery Address', max_length=100, default='', blank= True)

    deliveryDate =  models.DateField()
    suggPrice = models.DecimalField('Suggested Price', decimal_places=7,
                                max_digits=100, default=Decimal('0.00000'))

    #suggPrice = models.IntegerField("Suggested price/gallon", default =0)
    total = models.DecimalField('Total (Price * Gallons)', decimal_places=7,
                                max_digits=100, default=Decimal('0.00000'))  # total will be calculated by (suggPrice*gallsRequested)
  
    def __str__(self):
        return self.user.username
    
    
    
class PricingModule:
    def __init__(self, galls_req, user):
        self.current_price = 1.50
        self.galls_requested = galls_req
        self.user = user

    def state_factor(self):
        if self.user.userprofile.State == 'TX':
            return 0.02
        else:
            return 0.04

    def rate_history_factor(self):
        doesHistoryExist = UserFuelForm.objects.filter(user=self.user).exists()

        if doesHistoryExist:
            return 0.01 
        else:
            return 0.0
# Create your models here.
