from django import forms

from .models import Book
from datetime import datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'author',
            'cover_type',
            'title',
            'publisher',
            'page_count',
            'pub_date',
        ]

    pub_date = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1, datetime.now().year + 50))
    )
