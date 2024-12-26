from bookshelf.models import Book
# Command to delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))

# Expected output:
# []