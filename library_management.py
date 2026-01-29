class LibraryItem:
    def __init__(self, title):
        self.title = title

    def get_info(self):
        print("Library Item:", self.title)


class Book(LibraryItem):
    def get_info(self):
        print("Book Title:", self.title)


class Magazine(LibraryItem):
    def get_info(self):
        print("Magazine Title:", self.title)


# Polymorphism
items = [
    Book("Python Programming"),
    Magazine("Tech Monthly")
]

for item in items:
    item.get_info()
