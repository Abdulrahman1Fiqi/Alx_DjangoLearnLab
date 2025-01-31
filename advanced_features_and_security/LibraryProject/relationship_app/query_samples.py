from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return [book.title for book in books]

# Query 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return f"No librarian found for library '{library_name}'."

# Example Usage:
if __name__ == "__main__":
    print("Books by George Orwell:", books_by_author("George Orwell"))
    print("Books in Central Library:", books_in_library("Central Library"))
    print("Librarian for Central Library:", librarian_for_library("Central Library"))