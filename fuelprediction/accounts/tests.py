import unittest

from django.test import TestCase, Client
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm , UserChangeForm   
from .models import UserProfile, UserFuelForm
from .forms import RegistrationForm
import datetime


# Create your tests here.
class Test_home(TestCase):

    def test_statuscode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    
    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'accounts/home.html')

class Test_fuelhistory(TestCase):

    def test_statuscode(self):
        response = self.client.get('/fuelhistory/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/fuelhistory/')
        self.assertTemplateUsed(response, 'accounts/fuelhistory.html')
   
class Test_login(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')        
        test_user1.save()

    def test_get(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context['form'], AuthenticationForm())

        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_loginSuccess(self):
        response = self.client.post('/login/', {'username': 'testuser1', 'password': '1X<ISRUkw+tuK'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_loginUnsuccess(self):
        response = self.client.post('/login/', {'username': 'testuser1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertContains(response, 'Invalid username or password.')
        form = AuthenticationForm()
        self.assertFalse(form.is_valid())


class Test_register(TestCase):


    def test_get(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    not working rn
    def test_RegisterSuccess(self):
        response = self.client.post('/register/', {'username': 'testuser2',
        'password1': '1X<ISRUkw+tuK',
        'password2': '1X<ISRUkw+tuK'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')

    def test_RegisterUnsuccess(self):
        response = self.client.post('/register/', {'username':'testuser2',
        'password1':'1X<ISRUkw+tuK',
        'password2': 'wrongpassword' })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'The two password fields didn’t match.')

        form = RegistrationForm()
        self.assertFalse(form.is_valid())


