# -------------------------------
# Library Book Manager
# Concepts: Lists, Dictionaries, Functions
# -------------------------------

books = [
    {"Book ID": 1001, "Book Name": "Python", "Book Author": "Guido", "Book Price": 2000},
    {"Book ID": 1002, "Book Name": "Data Structures", "Book Author": "Mark", "Book Price": 2600},
    {"Book ID": 1003, "Book Name": "C", "Book Author": "Dennis", "Book Price": 3700}
]


# Add a new book to the library
def add_book():
    book_id = int(input("Enter the Book ID: "))
    book_name = input("Enter the Book Name: ")
    book_author = input("Enter the Book Author: ")
    book_price = int(input("Enter the Book Price: "))

    duplicate = False

    # Check whether the Book ID already exists
    for book in books:
        if book["Book ID"] == book_id:
            duplicate = True
            break

    if duplicate:
        print("\nDuplicate Book IDs are not allowed!")
    else:
        new_book = {
            "Book ID": book_id,
            "Book Name": book_name,
            "Book Author": book_author,
            "Book Price": book_price
        }

        books.append(new_book)
        print("\nBook Added Successfully!")


# Display all books
def view_book():
    if len(books) == 0:
        print("\nNo Books Available.")
        return

    print("\n" + "-" * 50)

    for book in books:
        print(f"Book ID     : {book['Book ID']}")
        print(f"Book Name   : {book['Book Name']}")
        print(f"Book Author : {book['Book Author']}")
        print(f"Book Price  : ${book['Book Price']}")
        print("-" * 50)


# Search a book using Book ID
def search_book():
    book_id = int(input("Enter the Book ID: "))

    for book in books:
        if book["Book ID"] == book_id:
            print("\nBook Found")
            print("-" * 30)
            print(f"Book ID     : {book['Book ID']}")
            print(f"Book Name   : {book['Book Name']}")
            print(f"Book Author : {book['Book Author']}")
            print(f"Book Price  : ${book['Book Price']}")
            return

    print("\nBook Not Found!")


# Delete a book using Book ID
def delete_book():
    book_id = int(input("Enter the Book ID: "))

    for book in books:
        if book["Book ID"] == book_id:
            books.remove(book)

            print("\nBook Deleted Successfully!")
            print("-" * 30)
            print(f"Book ID     : {book['Book ID']}")
            print(f"Book Name   : {book['Book Name']}")
            print(f"Book Author : {book['Book Author']}")
            print(f"Book Price  : ${book['Book Price']}")
            return

    print("\nBook Not Found!")


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n" + "=" * 50)
    print("          LIBRARY BOOK MANAGER")
    print("=" * 50)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")
    print("=" * 50)

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_book()

        elif choice == 2:
            view_book()

        elif choice == 3:
            search_book()

        elif choice == 4:
            delete_book()

        elif choice == 5:
            print("\nThank You! 💕")
            break

        else:
            print("\nPlease enter a valid choice (1-5).")

    except ValueError:
        print("\nError: Please enter a valid integer.")