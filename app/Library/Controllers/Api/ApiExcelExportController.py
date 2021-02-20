from django.http      import FileResponse, HttpResponse
from Library.models   import Book
from django.shortcuts import get_object_or_404
import time
import string
import environ
import xlsxwriter

env = environ.Env()
environ.Env.read_env()

cells_literals = string.ascii_uppercase
EXT            = '.xlsx'
STORAGE        = 'Library/storage/'

def exportBook(request, id):
    current_literal = 0
    file_name       = env('EXCEL_EXPORT_NAME') + EXT

    book  = get_object_or_404(Book, pk = id)
    cells = {
        'Название'    : book.title,
        'ФИО автора'  : str(book.author),
        'Страниц'     : book.page_count,
        'Год выпуска' : book.pub_date.strftime('%Y'),
        'Издатель'    : book.publisher,
    }

    workbook  = xlsxwriter.Workbook(STORAGE + file_name)
    worksheet = workbook.add_worksheet()

    for key, value in cells.items():
        literal = cells_literals[current_literal]
        worksheet.write(f'{literal}1', key)
        worksheet.write(f'{literal}2', value)
        current_literal += 1

    workbook.close()
    return FileResponse(open(STORAGE + file_name, 'rb'), as_attachment=True)