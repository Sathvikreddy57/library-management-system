class library:
    def __init__(self, listofbooks):
        self.books=listofbooks
    
    def displayavailablebooks(self):
        print('the books available in this library are:')
        print(', '.join(self.books)) #or we can eve use for loop to print books one by one with: for i in self.books, print(i)

    def addnewbooks(self,newbookslist): #we can even add singe book instead of list of books here
        self.books=self.books + newbookslist
    
    def addnewbook(self,newbook):
        self.books.append(newbook)
    
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f'you have borrowed the book {bookname}')
            self.books.remove(bookname)
        else:
            print('book not availabale try again later')

    def returnbook(self,bookname):
        self.books.append(bookname)
        print(f'you have returned the book {bookname}')

class student:
    def borrowbook(self):
        self.bookname=input("enter the book you want to borrow: ")
        return self.bookname
    
    def returnbook(self):
        self.bookname=input('enter the name of the book you want to return: ')
        return self.bookname


if __name__=='__main__':
    centralLibrary=library(['got','harrypotter','junglebook','tarzan','lionking'])
    student1=student()
    # centralLibrary.displayavailablebooks()
    # centralLibrary.addnewbooks(['apple','banana'])
    # centralLibrary.displayavailablebooks()
    # x=input('enter the book you want to borrow:')
    # centralLibrary.borrowbook(x)
    # centralLibrary.displayavailablebooks()
    # a=input('enter the book you want to add to the library:')
    # centralLibrary.addnewbook(a)
    # centralLibrary.displayavailablebooks()

    while(True):
        print("***********welcome to the sathvik's library***********")
        print('''        please choose an option:
              1. listing all the books available now
              2. borrow a book
              3. return a book
              4. exit the library''')
        
        a=int(input('enter your choice:'))

        match a:
            case 1:
                centralLibrary.displayavailablebooks()
            case 2:
                centralLibrary.borrowbook(student1.borrowbook())
            case 3:
                centralLibrary.returnbook(student1.returnbook())
            case 4:
                a=input("enter the book you want to add:")
                centralLibrary.addnewbook(a)
            case 5:
                print('thanks for using my library:')
                exit()
            case _:
                print('invalid choice\n')


'''
this is another outlook into making a library management system
You can make it menu driven by adding while(True) in the main function


class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.copies > 0:
            book.copies -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.copies += 1
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn, copies):
        new_book = Book(title, author, isbn, copies)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def add_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)
        print(f"Member '{name}' added to the library.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("Library Members:")
        for member in self.members:
            print(member)

# Example Usage
library = Library()

# Adding Books
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3)
library.add_book("1984", "George Orwell", "9780451524935", 2)

# Adding Members
library.add_member("Alice", "M001")
library.add_member("Bob", "M002")

# Displaying Books
library.display_books()

# Displaying Members
library.display_members()

# Borrowing Books
alice = library.find_member_by_id("M001")
gatsby = library.find_book_by_title("The Great Gatsby")

if alice and gatsby:
    alice.borrow_book(gatsby)

# Displaying Books after borrowing
library.display_books()

# Returning Books
if alice and gatsby:
    alice.return_book(gatsby)

# Displaying Books after returning
library.display_books()

'''