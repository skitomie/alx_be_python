class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {super().__str__()}, File Size: {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {super().__str__()}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

        """
        def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added {book}")
        else:
            print("Only books can be added to the library.")
        """

    def list_books(self):
        for book in self.books:
            print(book)