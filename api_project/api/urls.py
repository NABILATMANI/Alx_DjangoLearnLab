from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Task 1: URL routing for the basic BookList view
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# Task 2: Setting up the router for BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the router's URLs in the urlpatterns
urlpatterns += [
    path('', include(router.urls)),
]
