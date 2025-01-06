# blog/urls.py
from django.urls import path
from .views import post_list , register, user_login, user_logout, profile

urlpatterns = [
    path('', post_list, name='post_list'),
    path('posts/', post_list, name='post_list'), 
    path('register/', register, name='register'),
    path('login/', user_login),
]