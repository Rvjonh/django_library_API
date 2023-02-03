from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"
