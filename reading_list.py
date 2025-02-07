import csv
import sys

# Function to add a book to the reading list
def add_book(title, author, year):
        duplicate_found = False
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
            else:
                with open('books.csv', mode='a', newline='') as file:  # Open in append mode
                    writer = csv.writer(file)
                    writer.writerow([title, author, year])
                    print("Added Book Successfully")
        except FileNotFoundError:
            print("Error: 'books.csv' not found.")
            sys.exit()

#TODO: Write a "delete_book" function
# Function to delete a book from the reading list
def delete_book(title, author, year):
    books = []
    copy_found = False
    try:
        with open('books.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3 and title == row[0] and author == row[1] and year == row[2]:
                    copy_found = True
                else:
                    books.append(row)
                    print(books)

            if copy_found:
                with open('books.csv', mode='w', newline=''):
                    writer = csv.writer(file)
                    writer.writerow(books)
                    print("Book Removed Successfully")
            else:
                print("Book not found")

    except FileNotFoundError:
        print("Error adding books")
        sys.exit()



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
