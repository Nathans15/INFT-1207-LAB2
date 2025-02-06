import csv
import sys

# Function to add a book to the reading list
def add_book(title, author, year):
        # Boolean for if book the user tries
        # to add already exists in the list
        duplicate_found = False

        # Try/Except for if book file exists.
        # Operates normally if it does, tells user
        # an error happened adding books if not.
        try:
            with open('books.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                # For loop to identify possible dupilicates.
                # If duplicate found, set duplicate_found
                # boolean to True.
                for row in reader:
                    if title == row[0] and author == row[1] and year == row[2]:
                        duplicate_found = True

                # If statement activates after loop if duplicate_found
                # is True, letting user know of duplicate and notifies
                # them it cannot add the book. Else activates if
                # duplicate_found remains False, adding book normally.
                if duplicate_found:
                    print("Duplicate book found - Error adding books")
                else:
                    with open('books.csv', mode='a', newline=''):
                        writer = csv.writer(file)
                        writer.writerow([title, author, year])
        except FileNotFoundError:
            print("Error adding books")
            sys.exit()

#TODO: Write a "delete_book" function
# Function to delete a book from the reading list
def delete_book(title, author, year):
    try
        with open('books.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.deleterow([])



# Function to list all books
def list_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
    except FileNotFoundError:
        print("Error listing books")
        sys.exit()


# Function to search for a book by title
def search_book(title):
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == title.lower():
                    print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                    return
            print('Book not found')
    except FileNotFoundError:
        print("Error searching books")
        sys.exit()


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Quit")
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
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
