class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("\n📚 Library Books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")