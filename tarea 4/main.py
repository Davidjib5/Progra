from matriz import CMatFloat, crear_menu, leer_int, leer_float

def menu_operaciones(matriz_principal):
    """
    Submenú para operaciones con matrices
    """
    opciones = [
        "Sumar matrices",
        "Restar matrices", 
        "Volver al menú principal"
    ]
    
    while True:
        opcion = crear_menu(opciones)
        
        if opcion == 1:  # Sumar matrices
            if not matriz_principal.Existe():
                print("Error: Primero debes crear y llenar la matriz principal.")
                continue
            
            print("\n--- SUMAR MATRICES ---")
            print("Creando segunda matriz para la suma...")
            matriz2 = CMatFloat()
            
            # Crear matriz con las mismas dimensiones
            filas, columnas = matriz_principal.obtener_dimensiones()
            if filas == 1:  # Es una matriz 1D
                matriz2.CrearMatriziD(columnas)
            else:  # Es una matriz 2D
                matriz2.CrearMatriz2D(filas, columnas)
            
            print("Introduce los valores de la segunda matriz:")
            matriz2.Introducir()
            
            resultado = matriz_principal.SumarMatrices(matriz2)
            if resultado is not None:
                print("\n--- RESULTADO DE LA SUMA ---")
                print("Matriz 1:")
                matriz_principal.Mostrar()
                print("\nMatriz 2:")
                matriz2.Mostrar()
                print("\nSuma:")
                print(resultado)
        
        elif opcion == 2:  # Restar matrices
            if not matriz_principal.Existe():
                print("Error: Primero debes crear y llenar la matriz principal.")
                continue
            
            print("\n--- RESTAR MATRICES ---")
            print("Creando segunda matriz para la resta...")
            matriz2 = CMatFloat()
            
            # Crear matriz con las mismas dimensiones
            filas, columnas = matriz_principal.obtener_dimensiones()
            if filas == 1:  # Es una matriz 1D
                matriz2.CrearMatriziD(columnas)
            else:  # Es una matriz 2D
                matriz2.CrearMatriz2D(filas, columnas)
            
            print("Introduce los valores de la segunda matriz:")
            matriz2.Introducir()
            
            resultado = matriz_principal.RestarMatrices(matriz2)
            if resultado is not None:
                print("\n--- RESULTADO DE LA RESTA ---")
                print("Matriz 1:")
                matriz_principal.Mostrar()
                print("\nMatriz 2:")
                matriz2.Mostrar()
                print("\nResta:")
                print(resultado)
        
        elif opcion == 3:  # Volver al menú principal
            break

def main():
    """
    Función principal que ejecuta el programa
    """
    matriz_principal = CMatFloat()
    
    opciones_principales = [
        "Construir matriz 1D",
        "Construir matriz 2D", 
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar"
    ]
    
    print("="*60)
    print("          SISTEMA DE GESTIÓN DE MATRICES")
    print("="*60)
    
    while True:
        opcion = crear_menu(opciones_principales)
        
        if opcion == 1:  # Construir matriz 1D
            n_elementos = leer_int("Introduce el número de elementos para la matriz 1D: ")
            if n_elementos > 0:
                matriz_principal.CrearMatriziD(n_elementos)
            else:
                print("Error: El número de elementos debe ser mayor que 0.")
        
        elif opcion == 2:  # Construir matriz 2D
            filas = leer_int("Introduce el número de filas: ")
            columnas = leer_int("Introduce el número de columnas: ")
            if filas > 0 and columnas > 0:
                matriz_principal.CrearMatriz2D(filas, columnas)
            else:
                print("Error: Las filas y columnas deben ser mayores que 0.")
        
        elif opcion == 3:  # Introducir matriz
            matriz_principal.Introducir()
        
        elif opcion == 4:  # Mostrar matriz
            matriz_principal.Mostrar()
        
        elif opcion == 5:  # Operaciones con matrices
            menu_operaciones(matriz_principal)
        
        elif opcion == 6:  # Terminar
            print("\n¡Gracias por usar el sistema de gestión de matrices!")
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()