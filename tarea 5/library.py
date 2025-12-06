# library.py

from book import Book
from user import User
from typing import Optional

class Library:
    """
    Gestiona una colección de libros y usuarios, y las operaciones de préstamo.
    """
    def __init__(self):
        self.__books: dict[str, Book] = {} # ISBN -> Book object
        self.__users: dict[str, User] = {} # User ID -> User object

    def add_book(self, book: Book):
        """Agrega un nuevo libro a la biblioteca."""
        if book.isbn not in self.__books:
            self.__books[book.isbn] = book
            print(f"Libro '{book.title}' añadido correctamente.")
        else:
            print("Error: Ya existe un libro con ese ISBN.")

    def remove_book(self, isbn: str):
        """Elimina un libro de la biblioteca por su ISBN."""
        if isbn in self.__books:
            removed_book = self.__books.pop(isbn)
            print(f"Libro '{removed_book.title}' eliminado correctamente.")
        else:
            print("Error: No se encontró ningún libro con ese ISBN.")

    def register_user(self, user: User):
        """Registra un nuevo usuario en la biblioteca."""
        if user.user_id not in self.__users:
            self.__users[user.user_id] = user
            print(f"Usuario '{user.name}' (ID: {user.user_id}) registrado correctamente.")
        else:
            print("Error: El ID de usuario ya existe.")

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """Busca un libro por su ISBN."""
        return self.__books.get(isbn)

    def find_user_by_id(self, user_id: str) -> Optional[User]:
        """Busca un usuario por su ID."""
        return self.__users.get(user_id)

    def lend_book(self, isbn: str, user_id: str):
        """Presta un libro a un usuario."""
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_id(user_id)

        if not book:
            print("Error: El libro no existe.")
            return
        if not user:
            print("Error: El usuario no existe.")
            return
        
        if book.status == "disponible":
            book.status = "prestado"
            user.borrow_book(book)
            print(f"El libro '{book.title}' ha sido prestado a '{user.name}'.")
        else:
            print(f"Error: El libro '{book.title}' no está disponible.")

    def return_book(self, isbn: str, user_id: str):
        """Gestiona la devolución de un libro."""
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_id(user_id)

        if not book:
            print("Error: El libro no existe.")
            return
        if not user:
            print("Error: El usuario no existe.")
            return

        if book in user.borrowed_books:
            book.status = "disponible"
            user.return_book(book)
            print(f"El libro '{book.title}' ha sido devuelto por '{user.name}'.")
        else:
            print(f"Error: El usuario '{user.name}' no tiene prestado este libro.")

    def show_all_books(self):
        """Muestra todos los libros de la biblioteca."""
        if not self.__books:
            print("No hay libros en la biblioteca.")
            return
        print("\n--- Catálogo de Libros ---")
        for book in self.__books.values():
            print(book)
        print("------------------------")

    def show_all_users(self):
        """Muestra todos los usuarios registrados."""
        if not self.__users:
            print("No hay usuarios registrados.")
            return
        print("\n--- Lista de Usuarios ---")
        for user in self.__users.values():
            print(user)
        print("-------------------------")