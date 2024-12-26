# Command to retrieve the created book
book = Book.objects.get(title="1984")

# Output all attributes of the book
book_details = {
    "Title": book.title,
    "Author": book.author,
    "Publication Year": book.publication_year
}
print(book_details)

# Expected output:
# {'Title': '1984', 'Author': 'George Orwell', 'Publication Year': 1949}