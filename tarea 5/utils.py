# utils.py

import uuid
from typing import List, Dict, Callable

def generate_unique_id() -> str:
    """
    Genera un ID único de versión 4 y devuelve los primeros 8 caracteres.
    """
    return str(uuid.uuid4())[:8]

def leer_int(prompt: str) -> int:
    """
    Solicita un entero al usuario hasta que se ingrese uno válido.
    Genera un TypeError si el tipo del prompt no es el esperado.
    """
    if not isinstance(prompt, str):
        raise TypeError("El prompt debe ser una cadena de texto.")
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def crear_menu(titulo: str, opciones: Dict[str, Callable]):
    """
    Muestra un menú con un título y una lista de opciones.
    """
    print(f"\n--- {titulo} ---")
    for i, opcion in enumerate(opciones.keys(), 1):
        print(f"{i}. {opcion}")
    print("--------------------")