from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.new_book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.new_book.title, "A good title")
        self.assertEqual(self.new_book.subtitle, "An excellent subtitle")
        self.assertEqual(self.new_book.author, "Tom Christie")
        self.assertEqual(self.new_book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
