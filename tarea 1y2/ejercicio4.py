# Variable global para almacenar la lista de tareas
tareas = []

def add_task(task):
    """Agrega una nueva tarea a la lista global de tareas"""
    global tareas
    tareas.append(task)
    print(f"Tarea '{task}' agregada.")

def remove_task(task):
    """Elimina una tarea de la lista global de tareas si existe"""
    global tareas
    if task in tareas:
        tareas.remove(task)
        print(f"Tarea '{task}' eliminada.")
    else:
        print(f"Tarea '{task}' no encontrada.")

def list_tasks():
    """Lista todas las tareas en la lista global"""
    if not tareas:
        print("No hay tareas en la lista.")
        return
    print("Lista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")

def task_manager():
    """Administra las operaciones relacionadas con las tareas"""
    
    def modify_task():
        """Modifica la primera tarea de la lista"""
        nonlocal tareas_local
        if tareas_local:
            original = tareas_local[0]
            tareas_local[0] = original + " (modificada)"
            print(f"Tarea '{original}' modificada a '{tareas_local[0]}'.")
        else:
            print("No hay tareas para modificar.")

    global tareas
    tareas_local = tareas
    modify_task()
    tareas = tareas_local  # Guardamos los cambios

def main():
    while True:
        print("\n--- MENÚ DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Modificar primera tarea")
        print("4. Listar tareas")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            nueva_tarea = input("Ingrese la nueva tarea: ")
            add_task(nueva_tarea)
        elif opcion == "2":
            tarea_a_eliminar = input("Ingrese la tarea a eliminar: ")
            remove_task(tarea_a_eliminar)
        elif opcion == "3":
            task_manager()
        elif opcion == "4":
            list_tasks()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutamos el programa
main()
