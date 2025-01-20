"""
Using Builder Pattern

Each class method is a short form.

e.g. class `Book` contains methods:
    - with_author(author) -> Book
    - with_title(title) -> Book
    - with_year(year) -> Book
    - with_page(page) -> Book

"""

import copy
from typing import Self


class Page:
    content: str

    def __init__(self, content: str):
        self.content = content


class Book:
    author: str
    year: int
    title: str
    pages: list[Page]

    def __init__(self, author: str = None, year: int = None, title: str = None, pages: list[Page] = None):
        self.author = author
        self.title = title
        self.pages = pages
        self.year = year

    def with_author(self, author: str) -> Self:
        return Book(author, self.year, self.title, self.pages)

    def with_title(self, title: str) -> Self:
        return Book(self.author, self.year, title, self.pages)

    def with_year(self, year: int) -> Self:
        return Book(self.author, year, self.title, self.pages)

    def with_page(self, page: Page) -> Self:
        new_pages = copy.deepcopy(self.pages)
        if isinstance(new_pages, list):
            new_pages.append(page)
        else:
            new_pages = [page]
        return Book(self.author, self.year, self.title, new_pages)

def print_class(_class: object) -> None:
    print(_class)
    print(_class.__class__)
    print(_class.__dict__)
    print(_class.__hash__())


if __name__ == '__main__':
    b = Book()
    b1 = b.with_author('<NAME>')
    b2 = b1.with_year(1012)
    print_class(b)
    print_class(b1)
    print_class(b2)
