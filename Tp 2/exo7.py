from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self._name = name  #private attribute

    @property
    def name(self):
        return self._name

    @abstractmethod
    def info(self):
        pass

# Book class
class Book:
    def __init__(self, title, author):
        self._title = title  #private
        self._author = author
        self._is_borrowed = False

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if self._is_borrowed:
            raise Exception(f"'{self._title}' is already borrowed.")
        self._is_borrowed = True

    def return_book(self):
        self._is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"{self._title} by {self._author} - {status}"


class Member(Person):
    def __init__(self, name):
        super().__init__(name)
        self._borrowed_books = []

    def borrow_book(self, book):
        try:
            book.borrow()
            self._borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        except Exception as e:
            print(e)

    def return_book(self, book):
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def info(self):
        print(f"Member: {self.name}")


class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}'")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"Librarian {self.name} removed '{book.title}'")

    def info(self):
        print(f"Librarian: {self.name}")


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def remove_book(self, book):
        if book in self._books:
            if book.is_borrowed:
                print(f"Cannot remove '{book.title}'; it is currently borrowed.")
            else:
                self._books.remove(book)
        else:
            print(f"Book '{book.title}' not found in library.")

    def show_books(self):
        print("Library Books:")
        for book in self._books:
            print(book)


if __name__ == "__main__":
    library = Library()

    
    librarian = Librarian("Alice")
    member = Member("Bob")

    
    book1 = Book("1984", "George Orwell")
    book2 = Book("Python 101", "John Doe")
    librarian.add_book(library, book1)
    librarian.add_book(library, book2)

    library.show_books()

   
    member.borrow_book(book1)
    library.show_books()

    member.borrow_book(book1)

   
    member.return_book(book1)
    library.show_books()

    
    librarian.remove_book(library, book2)
    library.show_books()
