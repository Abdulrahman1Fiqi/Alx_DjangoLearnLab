# api/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)  # Field to store the author's name

    def __str__(self):
        return self.name  # String representation of the Author

class Book(models.Model):
    title = models.CharField(max_length=200)  # Field for the book's title
    publication_year = models.IntegerField()  # Field for the publication year
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key to Author

    def __str__(self):
        return self.title  # String representation of the Book