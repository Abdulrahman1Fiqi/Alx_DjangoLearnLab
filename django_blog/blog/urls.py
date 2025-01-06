# blog/urls.py
from django.urls import path
from .views import post_list , register, user_login, user_logout, profile

urlpatterns = [
    path('', post_list, name='post_list'),  # Home page
    path('register/', register, name='register'),  # Registration page
    path('login/', user_login, name='login'),  # Login page
    path('logout/', user_logout, name='logout'),  # Logout page
    path('profile/', profile, name='profile'),  # User profile page
]