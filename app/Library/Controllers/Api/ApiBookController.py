from Library.forms    import BookForm
from Library.models   import Book
from django.shortcuts import get_object_or_404, redirect
from django.http      import JsonResponse
from django.core      import serializers


def createBook(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
    return redirectToList()

def updateBook(request, id):
    book = get_object_or_404(Book, pk = id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
    return redirectToList()

def deleteBook(request, id):
    book = get_object_or_404(Book, pk = id)
    book.delete()
    return redirectToList()

def getList(request):
    return redirectToList()

def redirectToList():
    return redirect('/')