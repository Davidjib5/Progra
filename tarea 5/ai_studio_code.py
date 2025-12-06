# ejercicio1.py

import functools

def operation_logger(func):
    """
    Decorador que registra el nombre de una operación, sus entradas y el resultado.
    También maneja la división por cero.
    """
    @functools.wraps(func)
    def wrapper(operation, *args, **kwargs):
        op_name = operation.__name__.replace('<lambda>', 'lambda')
        print(f"--- Nueva Operación ---")
        print(f"Operación: {op_name}")
        print(f"Entradas: {args}")
        try:
            result = func(operation, *args, **kwargs)
            print(f"Resultado: {result}")
            print(f"----------------------\n")
            return result
        except ZeroDivisionError:
            print("Error: No es posible dividir por cero.")
            print(f"----------------------\n")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            print(f"----------------------\n")
    return wrapper

@operation_logger
def math_operation(operation, *args):
    """
    Toma una operación (función lambda) y un número variable de argumentos,
    y devuelve el resultado de aplicar la operación a los argumentos.
    """
    return operation(*args)

# ---------------------------------------------------------------------------
# Definición de funciones lambda para operaciones matemáticas básicas
# ---------------------------------------------------------------------------

# Suma que maneja múltiples argumentos
add = lambda *args: sum(args)

# Resta (definida para dos argumentos como en el ejemplo)
subtract = lambda x, y: x - y

# Multiplicación que maneja múltiples argumentos
def multiply_func(*args):
    if not args:
        return 0
    res = 1
    for val in args:
        res *= val
    return res
multiply = lambda *args: multiply_func(*args)


# División (definida para dos argumentos)
divide = lambda x, y: x / y

# ---------------------------------------------------------------------------
# Pruebas del sistema
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("### Probando el sistema de operaciones matemáticas ###\n")
    
    # Casos de prueba solicitados
    math_operation(add, 5, 3)
    math_operation(subtract, 10, 4)
    math_operation(multiply, 2, 6)
    math_operation(divide, 15, 3)
    
    # Prueba de manejo de división por cero
    math_operation(divide, 10, 0)
    
    # Prueba de manejo de múltiples argumentos
    math_operation(add, 1, 2, 3, 4, 5)
    math_operation(multiply, 2, 3, 4)