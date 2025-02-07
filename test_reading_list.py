import unittest
from reading_list import add_book, delete_book, list_books, search_book


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        add_book("Moby Dick", "Herman Melville", 1851)
        # Assert if the book is added (by manually checking CSV or creating validation logic)
    def test_add_book_2(self):
        add_book("Animal Farm", "George Orwell", 1949)

    def test_delete_book(self):
        delete_book("Brave New World", "Aldous Huxley", 1932)

    def test_search_book(self):
        search_book("Moby Dick")
        # Assert the output of the search

    # More test cases to be added...


if __name__ == '__main__':
    unittest.main()