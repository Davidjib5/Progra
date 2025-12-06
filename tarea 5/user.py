# user.py

from utils import generate_unique_id
from book import Book
from typing import List

class User:
    """
    Representa un usuario de la biblioteca con nombre, ID y libros prestados.
    """
    def __init__(self, name: str):
        self.__name = name
        self.__user_id = generate_unique_id()
        self.__borrowed_books: List[Book] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def user_id(self) -> str:
        return self.__user_id
        
    @property
    def borrowed_books(self) -> List[Book]:
        return self.__borrowed_books

    def borrow_book(self, book: Book):
        """Añade un libro a la lista de libros prestados del usuario."""
        if book not in self.__borrowed_books:
            self.__borrowed_books.append(book)

    def return_book(self, book: Book):
        """Elimina un libro de la lista de libros prestados."""
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)

    def __str__(self) -> str:
        """Visualización en forma de cadena de los datos del usuario."""
        borrowed_titles = [book.title for book in self.borrowed_books]
        return (f"Usuario: {self.name}, ID: {self.user_id}, "
                f"Libros Prestados: {borrowed_titles if borrowed_titles else 'Ninguno'}")