class Book:

    books = []

    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook:
    def __init__(self, Book, file_size):
        self.file_size = file_size
        self.Book = Book


class PrintBook:
    def __init__(self, Book, page_count):
        self.page_count = page_count
        self.Book = Book
        
class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.book = book

        Library.books.append(book)

    def list_books(self):
        for book in Library:
            print(book)