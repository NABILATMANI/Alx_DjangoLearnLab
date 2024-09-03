from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name='Author Name')
        self.book = Book.objects.create(title='Book Title', publication_year=2020, author=self.author)

    def test_create_book(self):
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        data = {'title': 'Updated Book', 'publication_year': 2022}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
