def imprimir_cadenas_con_letra(lista_cadenas):
    """Imprime cada cadena que comience con una letra específica"""
    letra = input("Ingrese la letra a buscar: ").lower()
    print(f"\nCadenas que comienzan con '{letra}':")
    encontradas = False
    for cadena in lista_cadenas:
        if cadena and cadena[0].lower() == letra:
            print(f"- {cadena}")
            encontradas = True
    if not encontradas:
        print("No se encontraron cadenas con esa letra inicial")

def contar_cadenas_con_subcadena(lista_cadenas):
    """Cuenta cuántas cadenas contienen una subcadena específica"""
    subcadena = input("Ingrese la subcadena a buscar: ")
    contador = 0
    for cadena in lista_cadenas:
        if subcadena in cadena:
            contador += 1
    print(f"\nNúmero de cadenas que contienen '{subcadena}': {contador}")

def encontrar_cadena_larga_corta(lista_cadenas):
    """Encuentra la cadena más larga y más corta"""
    if not lista_cadenas:
        print("La lista está vacía")
        return
    
    mas_larga = lista_cadenas[0]
    mas_corta = lista_cadenas[0]
    
    for cadena in lista_cadenas:
        if len(cadena) > len(mas_larga):
            mas_larga = cadena
        if len(cadena) < len(mas_corta):
            mas_corta = cadena
    
    print(f"\nCadena más larga: '{mas_larga}' ({len(mas_larga)} caracteres)")
    print(f"Cadena más corta: '{mas_corta}' ({len(mas_corta)} caracteres)")

def verificar_mismo_objeto(lista_cadenas):
    """Verifica si dos cadenas específicas son el mismo objeto usando is"""
    if len(lista_cadenas) < 2:
        print("Se necesitan al menos 2 cadenas en la lista")
        return
    
    print("Lista de cadenas:")
    for i, cadena in enumerate(lista_cadenas):
        print(f"{i}: {cadena}")
    
    try:
        indice1 = int(input("\nIngrese el índice de la primera cadena: "))
        indice2 = int(input("Ingrese el índice de la segunda cadena: "))
        
        if 0 <= indice1 < len(lista_cadenas) and 0 <= indice2 < len(lista_cadenas):
            cadena1 = lista_cadenas[indice1]
            cadena2 = lista_cadenas[indice2]
            
            print(f"\nCadena 1: '{cadena1}' (id: {id(cadena1)})")
            print(f"Cadena 2: '{cadena2}' (id: {id(cadena2)})")
            
            if cadena1 is cadena2:
                print("✅ Son el MISMO objeto (is retorna True)")
            else:
                print("❌ Son objetos DIFERENTES (is retorna False)")
                
            # Para comparación adicional
            if cadena1 == cadena2:
                print("📝 Tienen el mismo contenido (= = retorna True)")
            else:
                print("📝 Tienen contenido diferente (= = retorna False)")
        else:
            print("Índices fuera de rango")
    except ValueError:
        print("Por favor ingrese números válidos")

def verificar_longitud_mayor_10(lista_cadenas):
    """Verifica si alguna cadena tiene más de 10 caracteres usando for...else"""
    print("\nVerificando cadenas con longitud mayor a 10 caracteres:")
    
    for cadena in lista_cadenas:
        if len(cadena) > 10:
            print(f"✅ Encontrada: '{cadena}' ({len(cadena)} caracteres)")
            break
    else:
        # Este else se ejecuta solo si el bucle NO se rompió con break
        print("❌ Ninguna cadena tiene más de 10 caracteres")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print("MENÚ DE OPERACIONES CON CADENAS")
    print("="*50)
    print("1. Imprimir cadenas que comiencen con una letra")
    print("2. Contar cadenas con una subcadena")
    print("3. Encontrar cadena más larga y más corta")
    print("4. Verificar si dos cadenas son el mismo objeto")
    print("5. Verificar si hay cadenas con más de 10 caracteres")
    print("6. Salir")
    print("="*50)

def main():
    """Función principal del programa"""
    # Leer lista de cadenas desde teclado
    print("INGRESE LAS CADENAS (deje vacío y presione Enter para terminar):")
    lista_cadenas = []
    
    while True:
        cadena = input(f"Cadena {len(lista_cadenas) + 1}: ").strip()
        if cadena == "":
            break
        lista_cadenas.append(cadena)
    
    if not lista_cadenas:
        print("No se ingresaron cadenas. Saliendo...")
        return
    
    print(f"\nLista ingresada: {lista_cadenas}")
    
    # Menú principal
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            imprimir_cadenas_con_letra(lista_cadenas)
        elif opcion == "2":
            contar_cadenas_con_subcadena(lista_cadenas)
        elif opcion == "3":
            encontrar_cadena_larga_corta(lista_cadenas)
        elif opcion == "4":
            verificar_mismo_objeto(lista_cadenas)
        elif opcion == "5":
            verificar_longitud_mayor_10(lista_cadenas)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione 1-6.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()