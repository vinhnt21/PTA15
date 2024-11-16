class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                return True
        return False

    def show_books(self):
        if len(self.books) == 0:
            print("No book in the library")
        else:
            for book in self.books:
                print(book.name, book.author, book.price, book.qty)
