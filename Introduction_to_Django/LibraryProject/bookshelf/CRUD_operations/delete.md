### Step 6: Delete the Book Instance
Delete the book instance and confirm the deletion by trying to retrieve all books again. Document this in `delete.md`.

#### delete.md
```markdown
# Delete the Book

## Command
```python
retrieved_book.delete()
print("Book deleted successfully.")
all_books = Book.objects.all()
print(f"All Books: {all_books}") 


#Book deleted successfully.
#All Books: <QuerySet []>