from django.shortcuts import render

from books.models import Book


def get_all_books_html_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books_table.html', context)
