from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Router for CRUD operations
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # For Task 1: Basic API Endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # For Task 2: CRUD Operations
    path('', include(router.urls)),

    # For Task 3: Token Authentication
    path('api-token-auth/', include('rest_framework.authtoken.urls')),
]
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
