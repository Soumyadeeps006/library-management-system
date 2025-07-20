import tkinter as tk
from tkinter import messagebox
from library.library_manager import LibraryManager
from library.book import Book
from library.ebook import EBook
from library.audiobook import AudioBook

class LibraryGUI:
    def __init__(self, root):
        self.manager = LibraryManager()

        root.title("Library Management System")
        root.geometry("500x400")

        self.title_label = tk.Label(root, text="Title")
        self.title_label.pack()
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Author")
        self.author_label.pack()
        self.author_entry = tk.Entry(root, width=40)
        self.author_entry.pack()

        self.type_label = tk.Label(root, text="Book Type")
        self.type_label.pack()
        self.type_var = tk.StringVar(value="Book")
        self.type_menu = tk.OptionMenu(root, self.type_var, "Book", "EBook", "AudioBook")
        self.type_menu.pack()

        self.detail_label = tk.Label(root, text="File Size / Duration")
        self.detail_label.pack()
        self.detail_entry = tk.Entry(root, width=40)
        self.detail_entry.pack()

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=10)

        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        book_type = self.type_var.get()
        detail = self.detail_entry.get()

        if not title or not author:
            messagebox.showwarning("Input Error", "Please enter title and author.")
            return

        if book_type == "Book":
            book = Book(title, author)
        elif book_type == "EBook":
            if not detail.isdigit():
                messagebox.showwarning("Input Error", "File size must be a number.")
                return
            book = EBook(title, author, int(detail))
        elif book_type == "AudioBook":
            if not detail.isdigit():
                messagebox.showwarning("Input Error", "Duration must be a number.")
                return
            book = AudioBook(title, author, int(detail))

        self.manager.add_book(book)
        self.listbox.insert(tk.END, book.display())
        self.clear_inputs()

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.detail_entry.delete(0, tk.END)