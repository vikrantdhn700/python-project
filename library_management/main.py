""" Main module for the Library Management System (LMS). """

import lms


def main():
    """Main function to run the Library Management System."""

    books = lms.load_books()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. View Available Books")
        print("6. View All Books")
        print("7. View History")
        print("8. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                lms.add_book(books, title, author)

            elif choice == "2":
                book_id = input("Book ID: ")
                borrower = input("Borrower: ")
                lms.borrow_book(books, book_id, borrower)

            elif choice == "3":
                book_id = input("Book ID: ")
                lms.return_book(books, book_id)

            elif choice == "4":
                keyword = input("Search: ")
                lms.search_book(books, keyword)

            elif choice == "5":
                lms.view_available_books(books)

            elif choice == "6":
                lms.view_all_books(books)

            elif choice == "7":
                lms.display_history()

            elif choice == "8":
                break

            else:
                print("Invalid choice.")

        except (
            lms.LibraryManagementError,
            ValueError
        ) as error:
            print("Error:", error)
            lms.log_message(str(error), "error")


if __name__ == "__main__":
    main()
