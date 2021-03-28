from Library.forms    import BookForm
from Library.models   import Book
from django.shortcuts import get_object_or_404, redirect, render
from django.http      import JsonResponse, HttpResponse
from django.core      import serializers

VIEWS = {
    'createBook': 'Book/BookCreate.html',
    'updateBook': 'Book/BookUpdate.html',
    'deleteBook': 'Book/BookDelete.html',
    'detailBook': 'Book/BookDetail.html',
    'getList'   : 'Book/BookList.html',
}

VIEWS_ROUTES = {
    'createBook': 'book-create',
    'updateBook': 'book-update',
    'deleteBook': 'book-delete',
    'detailBook': 'book-detail',
    'getList'   : 'book-list',
}

def createBook(request):
    form = BookForm(request.POST)
    if form.is_valid():
        book = form.save()
        return redirect(VIEWS_ROUTES['detailBook'], id= book.id)
    else:
        return render(request, VIEWS['createBook'], {
            'form': form,
            'book': form.instance
        })

def updateBook(request, id):
    book = get_object_or_404(Book, pk = id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect(VIEWS_ROUTES['detailBook'], id= book.id)
    else:
        return render(request, VIEWS['updateBook'], {
            'form': form,
            'book': form.instance
        })

def deleteBook(request, id):
    book = get_object_or_404(Book, pk = id)
    book.delete()
    return redirectToList()

def getList(request):
    books = serializers.serialize('json', Book.objects.all())
    return HttpResponse(books, content_type='json')

def redirectToList():
    return redirect('book-list')