books = []


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")

    book = {
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("Book added successfully.")


def display_books():
    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        print(book["title"], "-", book["author"], "-", status)


def search_book():
    title = input("Enter book title: ")
    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            print("Book found.")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"])
            found = True

    if not found:
        print("Book not found.")


def borrow_book():
    title = input("Enter book title to borrow: ")
    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            found = True

            if book["available"]:
                book["available"] = False
                print("Book borrowed successfully.")
            else:
                print("Book is not available.")

    if not found:
        print("Book not found.")


def return_book():
    title = input("Enter book title to return: ")
    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            found = True

            if not book["available"]:
                book["available"] = True
                print("Book returned successfully.")
            else:
                print("Book was not borrowed.")

    if not found:
        print("Book not found.")


def remove_book():
    title = input("Enter book title to remove: ")
    found = False

    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("Book removed successfully.")
            found = True
            break

    if not found:
        print("Book not found.")

def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_book()

            case "2":
                display_books()

            case "3":
                search_book()

            case "4":
                borrow_book()

            case "5":
                return_book()

            case "6":
                remove_book()

            case "7":
                print("Exiting...")
                break

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()