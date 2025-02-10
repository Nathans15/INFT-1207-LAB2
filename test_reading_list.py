import unittest
from reading_list import add_book, delete_book, list_books, search_book


class TestReadingList(unittest.TestCase):
    def test_add_book_1(self):
        add_book("Moby Dick", "Herman Melville", 1851)
        with open(self.test_file, 'r') as file:
            books = file.readlines()
        self.assertIn("Moby Dick,Herman Melville,1851\n", books)
        # Assert if the book is added (by manually checking CSV or creating validation logic)
    def test_add_book_2(self):
        add_book("Animal Farm", "George Orwell", 1949)
        with open(self.test_file, 'r') as file:
            books = file.readlines()
        self.assertIn("Animal Farm,George Orwell,1949\n", books)
        # Assert if another book is added

    def test_duplicate_error(self):
        add_book("Moby Dick", "Herman Melville", 1851)
        with open(self.test_file, 'r') as file:
            books = file.readlines()
        self.assertIn()
        # TODO: The above should assert the associated error for duplicate books.
        # Check that duplicate books are not added

    def test_add_book(self):
        add_book("", "J.K. Rowling", "1997")
        # Expect error message: "Error adding book - Input field empty"

    def test_add_book(self):
        add_book("Dune", "Frank Herbert", "2030")
        # Expect error message: "Error adding book - Invalid year"

    def test_add_book(self):
        add_book("Moby Dick", "Herman Melville", "Eighteen Fifty-One")
        # Expect error message: "Error adding book - Year must be numerical"

    def test_delete_book(self):
        delete_book("The Great Gatsby", "F. Scott Fitzgerald", "1925")
        # Validate that the book is removed

    def test_delete_book(self):
        delete_book("Nonexistent Book", "Unknown Author", "2020")
        # Expect error message: "Book not found - Error deleting book"

    def test_search_book(self):
        search_book("To Kill a Mockingbird")
        # Expect: "Found - Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960"

    def test_search_book(self):
        search_book("A Book That Doesn't Exist")
        # Expect: "Error finding book - Book not found"

    def test_list_books(self):
        list_books()
        # Expect output listing books

    def test_add_book(self):
        add_book("2084", "Jon Orwell", "2084")
        # Expect error message: "Error adding book - Invalid year"



if __name__ == '__main__':
    unittest.main()