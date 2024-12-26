from django.shortcuts import render
# LibraryProject/bookshelf/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Logic to create a book
        pass
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Logic to edit the book
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Create your views here.

def book_search(request):
    query = request.GET.get('q')
    if query:
        # Use Django's ORM to filter results safely
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            published_date = form.cleaned_data['published_date']
            # Here you can save the data or perform other actions
            # For example, you might want to create a new Book instance
            # Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ExampleForm()  # Create a new form instance
    return render(request, 'bookshelf/example_form.html', {'form': form})