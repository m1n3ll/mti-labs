# Library System with OOP

#class author
class Author:
    def __init__(self, name):
        self.name = name  #self is a reference to the current object that’s calling the method

    def display_info(self):
        return f"Author: {self.name}"


#class book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author    
        self.year = year

    def display_info(self):
        return f"Book: '{self.title}' by {self.author.name} ({self.year})"


#subclass inherantance 
class EBook(Book):  
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size  

    # polymorphism
    def display_info(self):
        return f"E-Book: '{self.title}' by {self.author.name} ({self.year}) - {self.file_size}MB"


# class library 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f" '{book.title}' added to {self.name} library.")

    def show_books(self):
        print(f"\n Books in {self.name} Library:")
        for book in self.books:
            print(" -", book.display_info())

