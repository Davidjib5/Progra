import numpy as np

def leer_int(mensaje="Introduce un número entero: "):
    """
    Función auxiliar que lee un número entero del teclado.
    Si se introduce un valor no válido, se solicita de nuevo.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes introducir un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: "):
    """
    Función auxiliar que solicita al usuario un número decimal.
    Si se introduce un valor no válido, se solicita de nuevo.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes introducir un número decimal válido.")

def crear_menu(opciones_menu):
    """
    Función que muestra un menú de opciones y solicita al usuario que seleccione una opción válida.
    """
    print("\n" + "="*50)
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    print("="*50)
    
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if 1 <= opcion <= len(opciones_menu):
                return opcion
            else:
                print(f"Error: Debes seleccionar una opción entre 1 y {len(opciones_menu)}")
        except ValueError:
            print("Error: Debes introducir un número válido.")

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.
    """
    
    def __init__(self):
        """
        Método para inicializar el atributo matriz con None
        Y los atributos filas y columnas a 0.
        """
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0
    
    def CrearMatriz2D(self, nFilas, nColumnas):
        """
        Método para crear una matriz bidimensional de ceros.
        Asigna valores de filas y columnas según parámetros.
        """
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas
        print(f"Matriz 2D de {nFilas}x{nColumnas} creada correctamente.")
    
    def CrearMatriziD(self, nElementos):
        """
        Método para crear una matriz unidimensional de ceros.
        Usa CrearMatriz2D para asignar 1 fila y n columnas.
        """
        self.CrearMatriz2D(1, nElementos)
        print(f"Matriz 1D con {nElementos} elementos creada correctamente.")
    
    def Introducir(self):
        """
        Método para introducir los elementos de la matriz.
        Los elementos de la matriz son de tipo decimal.
        """
        if not self.Existe():
            print("Error: Primero debes crear una matriz.")
            return
        
        print(f"Introduce los elementos de la matriz ({self._m_nFilas}x{self._m_nColumnas}):")
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                mensaje = f"Elemento [{i}][{j}]: "
                self._Matriz[i][j] = leer_float(mensaje)
        
        print("Matriz introducida correctamente.")
    
    def Mostrar(self):
        """
        Método para mostrar los elementos de la matriz.
        """
        if not self.Existe():
            print("Error: No hay matriz creada para mostrar.")
            return
        
        print("\nMatriz actual:")
        print(self._Matriz)
    
    def Existe(self):
        """
        Método que verifica si matriz está creada y no está vacía.
        Retorna True si existe, de lo contrario retorna False.
        """
        return self._Matriz is not None and self._Matriz.size > 0
    
    def SumarMatrices(self, otra_matrix):
        """
        Método que suma la matriz actual con otra matriz.
        
        Parámetros:
        otra_matrix: objeto de CMatFloat con la matriz a sumar.
        
        Retorna:
        numpy.ndarray: La matriz resultante de la suma.
        """
        if not self.Existe() or not otra_matrix.Existe():
            print("Error: Ambas matrices deben estar creadas.")
            return None
        
        if self._m_nFilas != otra_matrix._m_nFilas or self._m_nColumnas != otra_matrix._m_nColumnas:
            print("Error: Las dimensiones de las matrices no coinciden.")
            return None
        
        return self._Matriz + otra_matrix._Matriz
    
    def RestarMatrices(self, otra_matrix):
        """
        Método que resta la matriz actual con otra matriz.
        
        Parámetros:
        otra_matrix: objeto de CMatFloat con la matriz a restar.
        
        Retorna:
        numpy.ndarray: La matriz resultante de la resta.
        """
        if not self.Existe() or not otra_matrix.Existe():
            print("Error: Ambas matrices deben estar creadas.")
            return None
        
        if self._m_nFilas != otra_matrix._m_nFilas or self._m_nColumnas != otra_matrix._m_nColumnas:
            print("Error: Las dimensiones de las matrices no coinciden.")
            return None
        
        return self._Matriz - otra_matrix._Matriz
    
    def obtener_dimensiones(self):
        """
        Método auxiliar para obtener las dimensiones de la matriz.
        """
        return self._m_nFilas, self._m_nColumnas