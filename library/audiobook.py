from library.book import Book

class AudioBook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration

    def display(self):
        return f"{super().display()}, Duration: {self.duration} mins (AudioBook)"