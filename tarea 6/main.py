from clases import Empleado, Cliente, RegistroDiario
from Time import Time
import Utils

def crear_hora():
    print("Introduzca hora de nacimiento:")
    h = Utils.leer_entero("Hora (1-12): ")
    m = Utils.leer_entero("Minutos (0-59): ")
    s = Utils.leer_entero("Segundos (0-59): ")
    ampm = Utils.leer_cadena("AM/PM: ").upper()
    return Time(h, m, s, ampm)

def main():
    registro = RegistroDiario()
    
    # Creamos un segundo registro dummy para probar la opción 7
    registro_extra = RegistroDiario()
    registro_extra.agregar_persona(Empleado("EmpleadoExtra", 30, Time(), "Auxiliar", 1))
    registro_extra.agregar_persona(Cliente("ClienteExtra", 25, Time(), "0000X"))

    opciones = [
        "Introducir empleado", "Introducir cliente", "Buscar por nombre (y edad)",
        "Mostrar registro diario", "Mostrar empleados", "Visualizar persona por índice",
        "Combinar registros diarios", "Salir"
    ]

    while True:
        opc = Utils.mostrar_menu(opciones)

        if opc == 1:
            nombre = Utils.leer_cadena("Nombre: ")
            edad = Utils.leer_entero("Edad: ")
            nacio = crear_hora()
            cat = Utils.leer_cadena("Categoría: ")
            ant = Utils.leer_entero("Antigüedad: ")
            e = Empleado(nombre, edad, nacio, cat, ant)
            registro.agregar_persona(e)
            print("Empleado añadido.")

        elif opc == 2:
            nombre = Utils.leer_cadena("Nombre: ")
            edad = Utils.leer_entero("Edad: ")
            nacio = crear_hora()
            dni = Utils.leer_cadena("DNI: ")
            c = Cliente(nombre, edad, nacio, dni)
            registro.agregar_persona(c)
            print("Cliente añadido.")

        elif opc == 3:
            nombre = Utils.leer_cadena("Nombre a buscar: ")
            preg_edad = input("¿Desea filtrar por edad? (s/n): ")
            edad = Utils.leer_entero("Edad: ") if preg_edad.lower() == 's' else None
            
            p = registro.buscar_persona(nombre, edad)
            if p:
                print("Persona encontrada:")
                print(p.Visualizar())
            else:
                print("Persona no encontrada.")

        elif opc == 4:
            registro.visualizar_registro()

        elif opc == 5:
            registro.visualizar_empleados()

        elif opc == 6:
            idx = Utils.leer_entero("Introduzca índice: ")
            try:
                # Uso del método mágico __getitem__
                persona = registro[idx] 
                print(persona.Visualizar())
            except IndexError:
                print("Error: Índice no válido.")

        elif opc == 7:
            print("Fusionando con registro extra (que contiene 2 personas)...")
            # Uso del método mágico __add__
            registro_total = registro + registro_extra
            print("Nuevo registro combinado:")
            registro_total.visualizar_registro()

        elif opc == 8:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()