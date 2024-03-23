from src.models.book import Book
from mysql.connector import connect

# book = Book(100, 'Half Girlfriend', "Chetan Bhagath", "available")

# print(book.book_id, book.book_name, book.author, book.status)

def get_connection():
    return connect(
        host="localhost", user="root", password="Aug2023", database="library"
    )


def menu():
    print("Welcome to the Library: ")
    print(
        """
    Menu Options:
          1. Add a Book to the library
          2. View all the books
          3. return the book
          4. delete a book
          5. Issue a Book
"""
    )


def add_book():
    book_id: int = int(input("book id please: "))
    book_name: str = input("enter the book name: ")
    author: str = input("enter author name: ")
    status: str = input("book status: ")

    connection = get_connection()
    cursor = connection.cursor()
    query = f"insert into books values({book_id}, '{book_name}', '{author}', '{status}')"

    cursor.execute(query)

    connection.commit()

    print("book added!")


def view_all_books():
    # take all books from database and result it
    print("book view!")


def return_book():
    # return a book (book_id, person_name)
    print("book return!")


def delete_book():
    # book_id
    print("book delete!")


def issue_book():
    # book_id, person_name
    print("book issue!")


while True:
    menu()
    try:
        user_input = int(input("what is your input? "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if user_input == 1:
        add_book()
    elif user_input == 2:
        view_all_books()
    elif user_input == 3:
        return_book()
    elif user_input == 4:
        delete_book()
    elif user_input == 5:
        issue_book()
    else:
        print("Invalid choice!!")
    try:
        choice: str = input("Do you want proceed further Y/N : ")
        if choice in ("n", "N", "no", "No", "NO", "nO"):
            break
        elif choice.lower() == "y":
            continue
        else:
            raise ValueError("Give vaid choice")
    except ValueError:
        print("please enter valid choice!")
