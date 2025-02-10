import unittest
from reading_list import add_book, delete_book, list_books, search_book


class TestReadingList(unittest.TestCase):

    def setUp(self):
        # Set up a CSV file and clear its contents before each test.
        self.test_file = "books.csv"
        with open(self.test_file, "w") as file:
            file.write("")

    def test_add_book_1(self):
        add_book("Moby Dick", "Herman Melville", "1851", self.test_file)
        with open(self.test_file, 'r') as file:
            books = file.readlines()
        self.assertIn("Moby Dick,Herman Melville,1851\n", books)


    def test_add_book_2(self):
        add_book("Animal Farm", "George Orwell", "1949", self.test_file)
        with open(self.test_file, 'r') as file:
            books = file.readlines()
        self.assertIn("Animal Farm,George Orwell,1949\n", books)

    def test_duplicate_error(self):
        add_book("Moby Dick", "Herman Melville", "1851")
        result = add_book("Moby Dick", "Herman Melville", "1851")
        self.assertEqual(result, "Duplicate book found - Error adding books")

    def test_empty_field_error(self):
        result = add_book("", "J.K. Rowling", "1997")
        self.assertEqual(result, "Error adding book - Input field empty")

    def test_invalid_year_error(self):
        result = add_book("Dune", "Frank Herbert", "-2030")
        self.assertEqual(result, "Error adding book - Invalid year")

    def test_invalid_year_error_2(self):
        result = add_book("2084", "Jon Orwell", "2084")
        self.assertEqual(result, "Error adding book - Invalid year")

    def test_NaN_error(self):
        result = add_book("Moby Dick", "Herman Melville", "Eighteen Fifty-One")
        self.assertEqual(result, "Error adding book - Year must be numerical")

    def test_delete_book(self):
        add_book("The Great Gatsby", "F. Scott Fitzgerald", "1925")
        delete_book("The Great Gatsby", "F. Scott Fitzgerald", "1925")
        with open(self.test_file, 'r') as file:
            books = file.readlines()
        self.assertNotIn("The Great Gatsby,F. Scott Fitzgerald,1925\n", books)

    def test_no_book_found_error(self):
        result = delete_book("Nonexistent Book", "Unknown Author", "2020")
        self.assertEqual(result, "Book not found - Error deleting book")

    def test_search_book(self):
        add_book("To Kill a Mockingbird", "Harper Lee", "1960")
        result = search_book("To Kill a Mockingbird")
        self.assertEqual(result, "Found - Title: To Kill a Mockingbird, Author: Harper Lee, Year: 1960")

    def test_search_not_found(self):
        result = search_book("A Book That Doesn't Exist")
        self.assertEqual(result, "Error finding book - Book not found")

    def test_list_books(self):
        # Test if listing books works correctly.
        add_book("The Hobbit", "J.R.R. Tolkien", "1937", self.test_file)
        add_book("1984", "George Orwell", "1949", self.test_file)
        result = list_books(self.test_file)
        expected_output = ("Title: The Hobbit, Author: J.R.R. Tolkien, Year: 1937\n"
                           "Title: 1984, Author: George Orwell, Year: 1949")
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()