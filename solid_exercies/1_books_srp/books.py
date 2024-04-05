class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    @staticmethod
    def pages_in_book(pages):
        if pages < 300:
            raise InvalidBook("The book is not finish yet, complete the pages!")
        return f"The book is finished"


class BookIsNotFound(Exception):
    pass


class InvalidBook(Exception):
    pass


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        try:
            title = next(filter(lambda b_title: b_title == title, self.books))
            self.books.remove(title)
        except StopIteration:
            raise BookIsNotFound("The book is not found in the library")

    def get_book_by_author(self, author):
        return [b for b in self.books if b.author == author]



