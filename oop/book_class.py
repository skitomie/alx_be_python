class Book:

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __del__(title, author, year):
        print(f"{title} by {author}, published in {year}")

    def __str__(title, author, year):
        return f"{title} by {author}, published in {year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"