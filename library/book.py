class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: '{self.title}' by {self.author} (File Size: {self.file_size}MB)"


class Audiobook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration

    def __str__(self):
        return f"Audiobook: '{self.title}' by {self.author} (Duration: {self.duration} mins)"