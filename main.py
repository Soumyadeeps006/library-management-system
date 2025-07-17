from library.book import Book, EBook, Audiobook
from library.library import Library

def main():
    library = Library()

    print("📚 Welcome to the Library Management System!")
    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. Add EBook")
        print("3. Add Audiobook")
        print("4. View All Books")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
            print("✅ Book added successfully!")

        elif choice == '2':
            title = input("Enter eBook title: ")
            author = input("Enter eBook author: ")
            file_size = input("Enter file size in MB: ")
            try:
                file_size = float(file_size)
                library.add_book(EBook(title, author, file_size))
                print("✅ EBook added successfully!")
            except ValueError:
                print("❌ Invalid file size. Please enter a number.")

        elif choice == '3':
            title = input("Enter audiobook title: ")
            author = input("Enter audiobook author: ")
            duration = input("Enter duration in minutes: ")
            try:
                duration = float(duration)
                library.add_book(Audiobook(title, author, duration))
                print("✅ Audiobook added successfully!")
            except ValueError:
                print("❌ Invalid duration. Please enter a number.")

        elif choice == '4':
            library.list_books()

        elif choice == '5':
            print("👋 Exiting the Library Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()