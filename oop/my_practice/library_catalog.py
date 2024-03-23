class Books:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

    def __str__(self):
        return f"Book {self.book_id}: {self.title} by {self.author}"


class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Author name: {self.name}"


class Catalog:
    def __init__(self):
        self.books = []
        self.authors = []

    def add_author(self, author):
        self.authors.append(author)

    def add_books(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def display_author(self):
        for author in self.authors:
            print(author)


if __name__ == "__main__":
    # Create Authors
    author1 = Author('John Smith')
    author2 = Author("Jane Doe")

    # Create Books

    book1 = Books("Python Programming", author1, "12wec11")
    book2 = Books("Data Science and Algorithm", author2, "300AB")

    # Create catalog
    library_catalog = Catalog()
    library_catalog.add_books(book1)
    library_catalog.add_books(book2)

    library_catalog.add_author(author1)
    library_catalog.add_author(author2)

    print("Book in the catalog: ")
    library_catalog.display_books()

    print("\nAuthor in the catalog: ")
    library_catalog.display_author()
