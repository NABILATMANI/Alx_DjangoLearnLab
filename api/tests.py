# tests.py

from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(title="Django for Beginners", author="William S. Vincent")

    def test_book_content(self):
        book = Book.objects.get(id=1)
        expected_title = f'{book.title}'
        expected_author = f'{book.author}'
        self.assertEqual(expected_title, 'Django for Beginners')
        self.assertEqual(expected_author, 'William S. Vincent')
