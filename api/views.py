# views.py

from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    data = {"books": list(books.values("title", "author"))}
    return JsonResponse(data)
