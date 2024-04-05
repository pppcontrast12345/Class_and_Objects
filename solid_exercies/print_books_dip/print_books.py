class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter:

    def format(self, book):
        return book.content[:4]


class Printer:

    def get_book(self, book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book



base_formatter = Formatter()
book_1 = Book("Some content")
paper_formatter = PaperFormatter()

p = Printer()
print(p.get_book(book_1, paper_formatter))