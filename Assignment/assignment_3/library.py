# 1️⃣ Simple Library Management System 📚

# Goal: Books aur Members manage karo.

# Abstraction: Base class Item (Book, Magazine)

# Encapsulation: Private fields for book availability or member fines

# Polymorphism: checkout() method behaves differently for Book vs Magazine

# Inheritance: Book and Magazine inherit from Item

from abc import abstractmethod

class Item:
    @abstractmethod
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        # availably is private
        
    def checkout(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
        
    def checkin(self):
        self.available = True
        
class Book(Item):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn
        
class Magazine(Item):
    def __init__(self, title, author, publication_date):
        super().__init__(title, author)
        self.publication_date = publication_date
        
class Library:
    def __init__(self):
        self.items = []
        self.members = []
        self.fines = {}

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, member):
        self.members.append(member)

    def checkout_item(self, item, member):
        if item.checkout():
            self.fines[member] = 0
            return True
        else:
            return False

student = Library()

book = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
magazine = Magazine("National Geographic", "National Geographic Society", "2022-01-01")

student.add_item(book)
student.add_item(magazine)

student.checkout_item(book, "John Doe")