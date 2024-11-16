from BookManager import BookManager
from Book import Book

book_manager = BookManager()
while True:
    print(
        """
          1. Add book
          2. Remove book
          3. Show books
          0. Exit
          """
    )
    choice = input("Enter your choice: ")
    if choice == "1":
        book_name = input("Enter book name: ")
        author = input("Enter author: ")
        price = int(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        book = Book(book_name, author, price, qty)
        book_manager.add_book(book)
    elif choice == "2":
        print("Remove book")
    elif choice == "3":
        book_manager.show_books()
    elif choice == "0":
        break
    else:
        print("Invalid choice")
