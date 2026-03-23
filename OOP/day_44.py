class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def book_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"


my_book = Book("Clean Code - Python", "Author Name", 2024)
