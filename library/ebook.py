from library.book import Book

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        return f"{super().display()}, File Size: {self.file_size}MB (EBook)"