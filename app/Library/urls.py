from django.urls import path

from .Controllers     import BookController
from .Controllers.Api import ApiBookController, ApiExcelExportController

urlpatterns = [
    path('',                BookController.list, name='book-list'),
    path('<int:id>/detail', BookController.detail, name='book-detail'),
    path('create/',         BookController.create, name='book-create'),
    path('<int:id>/update', BookController.update, name='book-update'),

    path('api/book/<int:id>/update', ApiBookController.updateBook,        name='api-book-update'),
    path('api/book/<int:id>/delete', ApiBookController.deleteBook,        name='api-book-delete'),
    path('api/book/create',          ApiBookController.createBook,        name='api-book-create'),
    path('api/book/list',            ApiBookController.getList,           name='api-book-list'),
    path('api/export/book/<int:id>', ApiExcelExportController.exportBook, name='api-export-book'),
]
