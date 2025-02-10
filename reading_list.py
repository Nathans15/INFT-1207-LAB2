import csv
import sys
import time
# Time is imported for year-checking, to make sure the user
# Cannot enter a year that hasn't been reached.

# Date: February 7th, 2025
# Authors: Spiro Kontossoros, Nathan Sheldrake
# Student IDs: 100843569 (Kontossoros), 100964827 (Sheldrake)
# Description: A library program that allows the user to add books,
# delete them, search for a specific book and list the entire library.

# Return statements under each error

# Constant for the current year
CURRENT_YEAR = time.localtime().tm_year

# Function to add a book to the reading list
def add_book(title, author, year):
        duplicate_found = False
        try:
            if title == '' or author == '' or year == '':
                print("Error adding book - Input field empty")
                return "Error adding book - Input field empty"
            elif int(year) <= 0 or CURRENT_YEAR < int(year):
                print("Error adding book - Invalid year")
                return "Error adding book - Invalid year"
            else:
                try:
                    # Open file in read mode to check for duplicates
                    with open('books.csv', mode='r', newline='') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if len(row) == 3 and title == row[0] and author == row[1] and year == row[2]:
                                duplicate_found = True

                    # If no duplicate found, append the new book
                    if duplicate_found:
                        print("Duplicate book found - Error adding books")
                        return "Duplicate book found - Error adding books"
                    else:
                        with open('books.csv', mode='a', newline='') as file:  # Open in append mode
                            writer = csv.writer(file)
                            writer.writerow([title, author, year])
                            print("Added Book Successfully")
                except FileNotFoundError:
                    print("Error: 'books.csv' not found.")
                    sys.exit()

        except ValueError:
            print("Error adding book - Year must be numerical")
            return "Error: adding book - Year must be numerical"

# Function to delete a book from the reading list
def delete_book(title, author, year):
    books = []
    # Boolean for checking if requested
    # book exists to delete
    copy_found = False
    try:
        if title == '' or author == '' or year == '' or int(year) <= 0:
            print("Error adding book - Input field empty")
            return "Error adding book - Input field empty"
        else:
            try:
                # Read book file to check for a copy of a book
                with open('books.csv', mode='r', newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if len(row) == 3 and title == row[0] and author == row[1] and year == row[2]:
                            copy_found = True
                            # Append other books
                        else:
                            books.append(row)
                            print(books)

                    if copy_found:
                        with open('books.csv', mode='w', newline='') as file:
                            writer = csv.writer(file)
                            # Write remaining books back to the file
                            writer.writerows(books)
                        print("Book Removed Successfully")
                        return "Book Removed Successfully"
                    else:
                        print("Book not found - Error deleting book")
                        return "Book not found - Error deleting book"

            except FileNotFoundError:
                print("Error deleting books")
                sys.exit()
    except ValueError:
        print("Error adding book - Invalid year")
        return "Error adding book - Invalid year"



# Function to list all books
def list_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
    except FileNotFoundError:
        print("Error listing books - Books not found")
        sys.exit()


# Function to search for a book by title
def search_book(title):
    try:
        if title == '':
            print("Error searching books - Empty input field")
        else:
            with open('books.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0].lower() == title.lower():
                        print(f'Found - Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                        return
                print('Error finding book - Book not found')
                return "Error finding book - Book not found"
    except FileNotFoundError:
        print("Error searching books")
    sys.exit()


# Menu loop
def menu():
    while True:
        print("\n1. Add Books\n2. List Books\n3. Search Book\n4. Delete Books\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)

        elif choice == '2':
            list_books()

        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)

        elif choice == '4':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            delete_book(title, author, year)

        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
