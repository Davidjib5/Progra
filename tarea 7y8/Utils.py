# Utils.py
import pickle
import os
from excepciones import ErrorArchivo

def leer_entero(mensaje):
    """Solicita un entero al usuario de forma robusta."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes introducir un número entero válido.")

def leer_cadena(mensaje):
    """Solicita una cadena no vacía."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error: El campo no puede estar vacío.")

def guardar_datos(datos, nombre_fichero):
    """Serializa la lista de objetos y la guarda en disco."""
    try:
        # 'wb' = Write Binary. Necesario para pickle.
        with open(nombre_fichero, 'wb') as f:
            pickle.dump(datos, f)
        print("Datos guardados correctamente.")
    except IOError as e:
        raise ErrorArchivo(f"No se pudo escribir en el archivo: {e}")

def cargar_datos(nombre_fichero):
    """Carga una lista de objetos desde disco."""
    if not os.path.exists(nombre_fichero):
        raise ErrorArchivo("El archivo no existe.")
    
    try:
        # 'rb' = Read Binary. Necesario para pickle.
        with open(nombre_fichero, 'rb') as f:
            datos = pickle.load(f)
            return datos
    except (IOError, pickle.PickleError) as e:
        raise ErrorArchivo(f"Error al leer o decodificar el archivo: {e}")