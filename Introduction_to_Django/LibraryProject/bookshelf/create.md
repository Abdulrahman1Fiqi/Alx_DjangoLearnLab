# Command to create a book instance
from app_name.models import Book  # Replace 'app_name' with your app name
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected output:
# <Book: 1984 by George Orwell>