# api/urls.py

from django.urls import path , include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookViewSet, CustomAuthToken

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)), 
    path('auth/token/', CustomAuthToken.as_view(), name='api-token-auth'),  # Token retrieval endpoint
]