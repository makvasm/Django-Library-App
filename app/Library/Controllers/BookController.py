from django.shortcuts      import render, get_object_or_404
from django.core.paginator import Paginator

from Library.models import Book, Author
from Library.forms  import BookForm

per_page = 2

def list(request):
    page_number = request.GET.get('page', 1)
    books       = Book.objects.filter()
    pages       = Paginator(books, per_page)
    books       = pages.get_page(page_number)
    context     = {
        'books': books,
        'pages': pages
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
