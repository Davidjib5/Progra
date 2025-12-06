# book.py

class Book:
    """
    Representa un libro con título, autor, ISBN y estado.
    """
    def __init__(self, title: str, author: str, isbn: str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__status = "disponible"  # por defecto, el libro está disponible

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, new_status: str):
        """Permite cambiar el estado del libro (ej: 'disponible', 'prestado')"""
        self.__status = new_status

    def __str__(self) -> str:
        """Visualización en forma de cadena de los datos del libro."""
        return (f"Título: {self.title}, Autor: {self.author}, "
                f"ISBN: {self.isbn}, Estado: {self.status}")