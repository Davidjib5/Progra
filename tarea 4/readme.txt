# Preguntas y Respuestas sobre la Práctica 4

## **Pregunta 1:**
¿Por qué en el método `CrearMatriziD` se llama al método `CrearMatriz2D` en lugar de crear la matriz 1D directamente?

**Respuesta:**
Porque en numpy, una matriz 1D se puede representar como una matriz 2D con 1 fila y N columnas. Esto permite mantener la consistencia en la estructura de datos y facilita las operaciones posteriores, ya que tanto matrices 1D como 2D tendrán el mismo formato (2D) internamente, simplificando los métodos de suma, resta y validación de dimensiones.

---

## **Pregunta 2:**
¿Qué sucede si intentamos sumar dos matrices con dimensiones diferentes y cómo maneja el programa esta situación?

**Respuesta:**
El programa detecta el error mediante la validación en los métodos `SumarMatrices` y `RestarMatrices`. Compara `self._m_nFilas` con `otra_matrix._m_nFilas` y `self._m_nColumnas` con `otra_matrix._m_nColumnas`. Si no coinciden, muestra el mensaje "Error: Las dimensiones de las matrices no coinciden." y retorna `None`, evitando que el programa falle y permitiendo al usuario corregir el error.

---

## **Pregunta 3:**
¿Por qué se utiliza `numpy.zeros` en lugar de `numpy.array` para crear las matrices iniciales?

**Respuesta:**
Se usa `numpy.zeros` porque inicializa la matriz con valores 0.0, lo que garantiza que todos los elementos tengan un valor definido desde el principio (tipo float). Si se usara `numpy.array` sin valores iniciales, podrían quedar valores indeterminados en memoria. Además, proporciona una base limpia para que el usuario luego introduzca sus propios valores mediante el método `Introducir`.

---

## **Pregunta 4:**
¿Cómo maneja el programa el caso cuando un usuario intenta mostrar una matriz que no ha sido creada?

**Respuesta:**
El método `Mostrar` primero llama al método `Existe()`, que verifica si `self._Matriz` no es `None` y si tiene elementos (`self._Matriz.size > 0`). Si la matriz no existe, muestra el mensaje "Error: No hay matriz creada para mostrar." y retorna sin intentar acceder a la matriz, previniendo así un error de ejecución.

---

## **Pregunta 5:**
¿Por qué las funciones `leer_int` y `leer_float` utilizan un bucle `while True` con manejo de excepciones?

**Respuesta:**
Para implementar un mecanismo robusto de validación de entrada. El bucle `while True` asegura que el programa no continúe hasta que el usuario introduzca un valor válido. El bloque `try-except` captura la excepción `ValueError` que se produce cuando se introduce un valor no numérico, mostrando un mensaje de error y solicitando nuevamente la entrada, garantizando así que el programa nunca falle por entrada incorrecta del usuario.

---

## **Pregunta 6:**
En el método `Introducir`, ¿por qué se usa un doble bucle `for` anidado para llenar la matriz?

**Respuesta:**
Porque necesita acceder a cada elemento individual de la matriz bidimensional. El primer bucle (`for i in range(self._m_nFilas)`) recorre las filas, y el segundo bucle (`for j in range(self._m_nColumnas)`) recorre las columnas. Esto permite solicitar al usuario cada valor específico para la posición `[i][j]`, asegurando que toda la matriz se llene completamente de manera organizada.

---

## **Pregunta 7:**
¿Cómo determina el programa si debe crear una matriz 1D o 2D cuando el usuario selecciona operaciones de suma/resta en el submenú?

**Respuesta:**
El programa verifica las dimensiones de la matriz principal existente llamando a `obtener_dimensiones()`. Si la matriz tiene 1 fila (`filas == 1`), asume que es una matriz 1D y llama a `CrearMatriziD`; de lo contrario, llama a `CrearMatriz2D`. Esto garantiza que la segunda matriz tenga exactamente las mismas dimensiones que la primera, requisito indispensable para las operaciones de suma y resta matricial.