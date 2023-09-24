from django.contrib import admin
from django.urls import path
from django.urls import include

from books.views import get_all_books_html_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_all_books_html_view),
]
