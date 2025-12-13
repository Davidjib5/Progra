def mostrar_menu(opciones):
    print("\n--- MENÚ ---")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    return leer_entero("Seleccione una opción: ")

def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor introduzca un número entero válido.")

def leer_cadena(mensaje):
    """Solicita una cadena y valida que no esté vacía."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacío.")