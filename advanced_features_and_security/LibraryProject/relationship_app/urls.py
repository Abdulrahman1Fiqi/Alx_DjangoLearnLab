from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.list_books, name='home'),  # Example home page view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    path('books/add/', views.add_book, name='add_book/'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book/'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]