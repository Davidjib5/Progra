def suma_total(numeros):
    """Calcula la suma total de todos los números de la lista."""
    return sum(numeros)


def suma_positivos_negativos(numeros):
    """Calcula la suma de los números positivos y negativos por separado."""
    suma_positivos = sum(n for n in numeros if n > 0)
    suma_negativos = sum(n for n in numeros if n < 0)
    return suma_positivos, suma_negativos


def encontrar_max_min(numeros):
    """Encuentra el número máximo y mínimo en la lista."""
    return max(numeros), min(numeros)


def son_unicos(numeros):
    """Comprueba si todos los números en la lista son únicos."""
    return len(set(numeros)) == len(numeros)


def comparar_positivos_negativos(numeros):
    """Devuelve un mensaje usando operador condicional según la cantidad de positivos y negativos."""
    positivos = sum(1 for n in numeros if n > 0)
    negativos = sum(1 for n in numeros if n < 0)
    return (
        "Hay más números positivos." if positivos > negativos else
        "Hay más números negativos." if negativos > positivos else
        "Hay la misma cantidad de números positivos y negativos."
    )


def mostrar_menu():
    """Muestra las opciones del menú."""
    print("\n--- Menú de operaciones ---")
    print("1. Sumar todos los números")
    print("2. Sumar positivos y negativos por separado")
    print("3. Encontrar el número máximo y mínimo")
    print("4. Comprobar si todos los números son únicos")
    print("5. Comparar cantidad de positivos y negativos")
    print("6. Salir")


def main():
    # Leer lista de números del usuario
    entrada = input("Introduce una lista de números enteros separados por espacios: ")
    numeros = list(map(int, entrada.split()))

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            total = suma_total(numeros)
            print(f"Suma total: {total}")

        elif opcion == "2":
            positivos, negativos = suma_positivos_negativos(numeros)
            print(f"Suma de positivos: {positivos}")
            print(f"Suma de negativos: {negativos}")

        elif opcion == "3":
            maximo, minimo = encontrar_max_min(numeros)
            print(f"Máximo: {maximo}")
            print(f"Mínimo: {minimo}")

        elif opcion == "4":
            if son_unicos(numeros):
                print("Todos los números son únicos.")
            else:
                print("Hay números repetidos en la lista.")

        elif opcion == "5":
            mensaje = comparar_positivos_negativos(numeros)
            print(mensaje)

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 6.")


# Ejecutar el programa
main()
