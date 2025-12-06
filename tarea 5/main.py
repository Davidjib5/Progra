# main.py

from library import Library
from book import Book
from user import User
import utils

def main():
    """
    Función principal que ejecuta el menú de la biblioteca.
    """
    biblioteca = Library()

    # Datos iniciales para demostración
    biblioteca.add_book(Book("Cien Años de Soledad", "Gabriel García Márquez", "978-0307350438"))
    biblioteca.add_book(Book("El Señor de los Anillos", "J.R.R. Tolkien", "978-8445071793"))
    biblioteca.register_user(User("Ana Torres"))
    biblioteca.register_user(User("Carlos Gomez"))


    while True:
        print("\n===== MENÚ DE LA BIBLIOTECA =====")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Registrar usuario")
        print("4. Realizar préstamo")
        print("5. Realizar devolución")
        print("6. Mostrar todos los libros")
        print("7. Mostrar todos los usuarios")
        print("8. Salir")
        print("=================================")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            biblioteca.add_book(Book(titulo, autor, isbn))

        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.remove_book(isbn)

        elif opcion == '3':
            nombre = input("Nombre del nuevo usuario: ")
            biblioteca.register_user(User(nombre))

        elif opcion == '4':
            isbn = input("ISBN del libro a prestar: ")
            user_id = input("ID del usuario: ")
            biblioteca.lend_book(isbn, user_id)

        elif opcion == '5':
            isbn = input("ISBN del libro a devolver: ")
            user_id = input("ID del usuario que devuelve: ")
            biblioteca.return_book(isbn, user_id)

        elif opcion == '6':
            biblioteca.show_all_books()

        elif opcion == '7':
            biblioteca.show_all_users()

        elif opcion == '8':
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()