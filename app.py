from utils import database

#  menu options

USER_MENU="""
Enter:
'a'-Add a new book
'l'-List all books
'r'-Mak a book as read
'd'-Delete a book
'q'-Quit

Your Choice:"""

# create the menu function
def menu():
    # create a table here in the database
    database.create_table()
    
    # get the user choice
    user_choice = input(USER_MENU)
    
    while user_choice != 'q':
        if user_choice == 'a':
            prompt_add_book()
        elif user_choice == 'l':
            list_books()
        elif user_choice == 'r':
            prompt_read_book()
            
        elif user_choice == 'd':
            pass
        else:
            print("Invalid Choice, Please try again!")
        user_choice = input(USER_MENU)
        
    
# a function to prompt the user for the book name and author
def prompt_add_book():
    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")
    database.add_book(title,author)
    
# a function to list all books
def list_books():
    books_count = database.count_books()
    s = "s" if books_count == 0 or books_count >  1 else ""
    print(f"You have {books_count} book{s} in yor bookstore. ")
    
    books = database.get_all_book_from_db()
    for id,  book in enumerate(books, start=1):
        read = "Yes" if book[3] == 1 else "No"
        print(f"{book[0]}. {book[1]} written by {book[2]}, read: {read}")
        
# prompt function to mark the book as read
def prompt_read_book():
    title = input("Enter the title of the book you've finished reading: ")
    database.update_book(title)
    

# prompt function to delete a book
def prompt_delete_book():
    title = input("Enter the title of the book you wish to delete: ")
    database.delete_book(title)

# call the menu function here
menu()