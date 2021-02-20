from django.shortcuts import render, get_object_or_404

from Library.models import Book, Author
from Library.forms  import BookForm

def list(request):
    books = Book.objects.filter()
    context = {
        'books': books
    }
    return render(request, 'Book/BooksList.html', context)

def detail(request, id):
    book    = get_object_or_404(Book, pk= id)
    context = {
        'book': book
    }
    return render(request, 'Book/BookDetail.html', context)

def create(request):
    form = BookForm
    context = {
        'form': form
    }
    return render(request, 'Book/BookCreate.html', context)

def update(request, id):
    book = get_object_or_404(Book, pk= id)
    form = BookForm(instance=book)
    context = {
        'form': form,
        'book': book
    }
    return render(request, 'Book/BookUpdate.html', context)
