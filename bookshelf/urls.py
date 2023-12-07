from django.contrib import admin
from django.urls import path
from books.views import display_book_by_id_with_http, display_books_with_http, display_books_with_json, display_book_by_id_with_json

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', display_books_with_http),
    path('books/<int:book_id>/', display_book_by_id_with_http),
    path('api/books/', display_books_with_json),
    path('api/books/<int:book_id>/', display_book_by_id_with_json)
]
