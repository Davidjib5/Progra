# main.py
from clases import Libro, Revista
import Utils
from excepciones import ErrorBiblioteca

def main():
    biblioteca = [] # Lista para almacenar los objetos (Polimorfismo)

    while True:
        print("\n--- GESTIÓN DE BIBLIOTECA ---")
        print("1. Añadir publicación")
        print("2. Mostrar publicaciones")
        print("3. Guardar en fichero")
        print("4. Cargar de fichero")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                tipo = input("¿Es (1) Libro o (2) Revista?: ")
                titulo = Utils.leer_cadena("Título: ")
                autor = Utils.leer_cadena("Autor: ")
                anio = Utils.leer_entero("Año: ")

                if tipo == "1":
                    genero = Utils.leer_cadena("Género: ")
                    # Instanciación de clase derivada Libro
                    nuevo_obj = Libro(titulo, autor, anio, genero)
                elif tipo == "2":
                    edicion = Utils.leer_entero("Número de edición: ")
                    # Instanciación de clase derivada Revista
                    nuevo_obj = Revista(titulo, autor, anio, edicion)
                else:
                    print("Tipo no válido.")
                    continue

                biblioteca.append(nuevo_obj)
                print("Publicación añadida con éxito.")

            except ErrorBiblioteca as e:
                # Capturamos nuestras excepciones de validación (setters)
                print(f"Error de validación: {e}")

        elif opcion == "2":
            if not biblioteca:
                print("La biblioteca está vacía.")
            else:
                for pub in biblioteca:
                    # POLIMORFISMO: Se llama al método descripcion() 
                    # correspondiente al tipo de objeto (Libro o Revista)
                    print(pub.descripcion())

        elif opcion == "3":
            nombre = Utils.leer_cadena("Nombre del fichero (ej: datos.pkl): ")
            try:
                Utils.guardar_datos(biblioteca, nombre)
            except ErrorBiblioteca as e:
                print(f"Error al guardar: {e}")

        elif opcion == "4":
            nombre = Utils.leer_cadena("Nombre del fichero a cargar: ")
            try:
                biblioteca = Utils.cargar_datos(nombre)
                print(f"Se han cargado {len(biblioteca)} publicaciones.")
            except ErrorBiblioteca as e:
                print(f"Error al cargar: {e}")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta.")

if __name__ == "__main__":
    main()