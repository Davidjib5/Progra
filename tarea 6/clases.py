from Time import Time

# --- CLASE BASE ---
class Ficha:
    def __init__(self, nombre="", edad=0, nacio=None):
        self._nombre = nombre
        self._edad = edad
        # Si no se pasa hora, por defecto 12:00:00 AM
        self._nacio = nacio if nacio else Time(12, 0, 0, "AM")

    # Decoradores (Getters y Setters)
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, val):
        self._nombre = val

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, val):
        self._edad = val

    @property
    def nacio(self):
        return self._nacio
    
    @nacio.setter
    def nacio(self, val):
        self._nacio = val

    def Visualizar(self):
        # Método base
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nació a las: {self.nacio}"


# --- CLASES DERIVADAS ---
class Empleado(Ficha):
    def __init__(self, nombre, edad, nacio, categoria, antiguedad):
        # Llamada al constructor de la clase padre
        super().__init__(nombre, edad, nacio)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self): return self._categoria
    
    @categoria.setter
    def categoria(self, val): self._categoria = val

    @property
    def antiguedad(self): return self._antiguedad
    
    @antiguedad.setter
    def antiguedad(self, val): self._antiguedad = val

    # Polimorfismo: Sobrescritura de Visualizar
    def Visualizar(self):
        base_info = super().Visualizar()
        return f"[EMPLEADO] {base_info}, Categoría: {self.categoria}, Antigüedad: {self.antiguedad} años"


class Cliente(Ficha):
    def __init__(self, nombre, edad, nacio, dni):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self): return self._dni
    
    @dni.setter
    def dni(self, val): self._dni = val

    # Polimorfismo: Sobrescritura de Visualizar
    def Visualizar(self):
        base_info = super().Visualizar()
        return f"[CLIENTE] {base_info}, DNI: {self.dni}"

    # Sobrecarga de operadores: Comparación (==)
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.nombre == other.nombre and self.edad == other.edad
        return False


# --- CLASE GESTORA ---
class RegistroDiario:
    def __init__(self):
        self._personas = [] # Lista polimórfica (guarda Empleados y Clientes)

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
        else:
            print("Error: Solo se pueden agregar objetos Empleado o Cliente.")

    def visualizar_registro(self):
        if not self._personas:
            print("El registro está vacío.")
        for p in self._personas:
            # Polimorfismo: llama al método Visualizar específico de la clase del objeto
            print(p.Visualizar())

    def visualizar_empleados(self):
        print("--- Lista de Empleados ---")
        encontrado = False
        for p in self._personas:
            if self.es_empleado(p):
                print(p.Visualizar())
                encontrado = True
        if not encontrado:
            print("No hay empleados registrados.")

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    # Sobrecarga de operador de indexación []
    def __getitem__(self, index):
        if 0 <= index < len(self._personas):
            return self._personas[index]
        else:
            raise IndexError("Índice fuera de rango en el registro.")

    # Sobrecarga de operador suma +
    def __add__(self, other):
        if isinstance(other, RegistroDiario):
            nuevo_registro = RegistroDiario()
            # Combina las listas de ambos registros
            nuevo_registro._personas = self._personas + other._personas
            return nuevo_registro
        return NotImplemented
    
    def buscar_persona(self, nombre, edad=None):
        for p in self._personas:
            # Si edad se proporciona, busca por ambos, si no, solo nombre
            if p.nombre.lower() == nombre.lower():
                if edad is None or p.edad == int(edad):
                    return p
        return None