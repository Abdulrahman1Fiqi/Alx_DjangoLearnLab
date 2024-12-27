# api/serializers.py

from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']  # Include all fields

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        if value > 2023:  # Replace with the current year if needed
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include the name and nested books