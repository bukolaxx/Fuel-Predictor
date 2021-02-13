from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name= 'login'),
    path('profile/', views.profile, name= 'profile'),
    path('edit_profile/', views.edit_profile, name= 'edit_profile'),
]