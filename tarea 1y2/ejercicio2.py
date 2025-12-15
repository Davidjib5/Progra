import math

def is_prime(n):
    """
    Comprueba si un número 'n' es primo.

    Un número primo es un número natural mayor que 1 que tiene solo dos
    divisores distintos: 1 y él mismo.

    :param n: El número entero a comprobar.
    :type n: int
    :return: True si el número es primo, False en caso contrario.
    :rtype: bool
    """
    if n < 2:
        return False
    # Solo necesitamos comprobar divisibilidad hasta la raíz cuadrada de n.
    # 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(limit):
    """
    Genera una lista de números primos hasta un límite 'limit' (incluido).

    :param limit: El límite superior (inclusive) para la búsqueda de primos.
    :type limit: int
    :return: Una lista de números primos hasta 'limit'.
    :rtype: list[int]
    """
    if limit < 2:
        return []
    
    primes = []
    # Usaremos la función is_prime() para la comprobación.
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def check_palindrome(primes):
    """
    Busca palíndromos en una lista de números primos.

    Un palíndromo es un número (o string) que se lee igual de adelante hacia atrás.
    Ejemplo: 101, 313.

    :param primes: Una lista de números primos.
    :type primes: list[int]
    :return: Una lista de números primos palíndromos encontrados.
    :rtype: list[int]
    """
    palindromes = []
    for prime in primes:
        # Convertir el número a string para facilitar la comprobación de palíndromo
        s = str(prime)
        # Comprobar si el string es igual a su reverso
        if s == s[::-1]:
            palindromes.append(prime)
    return palindromes

def categorize_prime(prime):
    """
    Clasifica un número primo en "pequeño", "mediano" o "grande".

    - Pequeño: Menor que 10
    - Mediano: De 10 a 99 (inclusive)
    - Grande: 100 o más

    :param prime: El número primo a clasificar.
    :type prime: int
    :return: La categoría del número primo ("pequeño", "mediano" o "grande").
    :rtype: str
    """
    if prime < 10:
        return "pequeño"
    elif 10 <= prime <= 99:
        return "mediano"
    else:  # prime >= 100
        return "grande"

def main():
    """
    Función principal para probar las funciones del programa.
    """
    print("--- 🔬 Análisis de Números Primos ---")
    print("-" * 35)

    # --- 1. Prueba de is_prime(n) ---
    test_numbers = [7, 12, 17, 1, 0, 97, 100]
    print("\n## 1. Comprobación de Primalidad (is_prime):")
    for num in test_numbers:
        print(f"¿Es {num} primo? -> {is_prime(num)}")

    # --- 2. Prueba de prime_list(limit) ---
    limit = 50
    print(f"\n## 2. Generación de Lista de Primos (hasta {limit}):")
    list_of_primes = prime_list(limit)
    print(list_of_primes)

    # --- 3. Prueba de check_palindrome(primes) ---
    # Usaremos la lista generada, que incluye primos palíndromos como 2, 3, 5, 7, 11
    # y si el límite fuera mayor, incluiría 101, 131, etc.
    print("\n## 3. Búsqueda de Palíndromos Primos:")
    palindromic_primes = check_palindrome(list_of_primes)
    print(f"Primos palíndromos hasta {limit}: {palindromic_primes}")

    # --- 4. Prueba de categorize_prime(prime) ---
    print("\n## 4. Clasificación de Primos (categorize_prime):")
    # Agregamos algunos números grandes para la prueba
    extended_primes = prime_list(200) 
    
    # Elegir algunos para probar las 3 categorías
    sample_primes = [2, 17, 101, 7, 97, 151] 
    
    for prime in sample_primes:
        category = categorize_prime(prime)
        print(f"El primo {prime} se clasifica como: **{category}**")

# Ejecutar la función main
if __name__ == "__main__":
    main()