### Step 4: Retrieve the Book You Created
Retrieve and display all attributes of the book you just created. Document this in `retrieve.md`.

#### retrieve.md
```markdown
# Retrieve the Book

## Command
```python
retrieved_book = Book.objects.get(id=new_book.id)
print(f"Retrieved Book: {retrieved_book}")
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Published Date: {retrieved_book.published_date}")

#Retrieved Book: Book object (1)
#Title: 1984, Author: George Orwell, Published Date: 1949-01-01