from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Task 1: Building Your First API Endpoint
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2: Implementing CRUD Operations with ViewSets and Routers
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
