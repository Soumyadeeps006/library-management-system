class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Title: {self.title}, Author: {self.author}, (Book)"