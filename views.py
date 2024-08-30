<<<<<<< HEAD
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
=======
# views.py

from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    data = {"books": list(books.values("title", "author"))}
    return JsonResponse(data)
>>>>>>> origin/main
