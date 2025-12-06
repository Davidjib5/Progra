# PREGUNTAS Y RESPUESTAS SOBRE LA PRÁCTICA 5

# --- Ejercicio 1: Operaciones Matemáticas ---

Pregunta 1: ¿Cuál es el propósito del decorador `@functools.wraps(func)` dentro de `operation_logger`?
Respuesta: Su propósito es preservar los metadatos de la función original (`math_operation`) cuando esta es decorada. Sin `@functools.wraps`, el nombre de la función `math_operation`, su documentación (`__doc__`) y otros atributos internos serían reemplazados por los de la función `wrapper`. Esto es crucial para la depuración y para mantener la introspección del código intacta.

Pregunta 2: En la función `math_operation`, ¿qué representa el parámetro `*args` y por qué es útil?
Respuesta: El parámetro `*args` permite que la función acepte un número variable de argumentos posicionales. Recolecta todos los argumentos adicionales en una tupla. Es útil en este contexto porque las diferentes operaciones matemáticas pueden requerir un número distinto de operandos; por ejemplo, la resta puede usar dos, mientras que la suma puede operar sobre múltiples números a la vez (`add(1, 2, 3, 4)`).

Pregunta 3: ¿Por qué se optó por usar funciones lambda para las operaciones? ¿Qué ventaja ofrecen frente a funciones normales definidas con `def`?
Respuesta: Las funciones lambda se utilizan para crear funciones anónimas y cortas en una sola línea. La ventaja principal aquí es la concisión: permiten definir operaciones simples como `add = lambda *args: sum(args)` de forma muy compacta. Son ideales para operaciones que no requieren una lógica compleja, documentación extensa o múltiples sentencias, haciendo el código más directo para estos casos de uso específicos.

# --- Ejercicio 2: Sistema de Gestión de Biblioteca ---

Pregunta 4: En las clases `Book` y `User`, ¿qué ventaja ofrece usar el decorador `@property` en lugar de hacer los atributos públicos (ej. `self.title`)?
Respuesta: El decorador `@property` implementa el principio de encapsulación. Permite tratar un método como un atributo de solo lectura, ocultando el atributo privado subyacente (ej. `self.__title`). Esto protege los datos de modificaciones accidentales desde fuera de la clase. Además, si en el futuro se necesitara añadir lógica al obtener o establecer un valor (como validaciones), se podría hacer modificando el método sin cambiar la forma en que se accede al atributo desde el exterior.

Pregunta 5: ¿Cuál es la función del módulo `uuid` en `utils.py` y por qué se utiliza `uuid.uuid4()` específicamente?
Respuesta: El módulo `uuid` se utiliza para generar identificadores únicos universales. La función `uuid.uuid4()` genera un UUID aleatorio de versión 4. Se utiliza específicamente esta función porque garantiza un alto grado de unicidad con una probabilidad de colisión extremadamente baja, lo que es perfecto para crear IDs únicos para usuarios y libros sin necesidad de un contador centralizado o de consultar una base de datos para verificar la disponibilidad del ID.

Pregunta 6: En la clase `Library`, se usan diccionarios para `self.__books` y `self.__users`. ¿Qué ventaja tiene usar un diccionario en lugar de una lista para esta tarea?
Respuesta: La principal ventaja es la eficiencia en la búsqueda. Al usar el ISBN o el ID de usuario como clave del diccionario, la búsqueda de un libro o usuario específico se realiza en tiempo promedio constante, O(1). Si se usara una lista, habría que recorrerla para encontrar un elemento, lo que resultaría en un tiempo de búsqueda lineal, O(n), que es mucho más lento a medida que la colección de libros o usuarios crece.

Pregunta 7: ¿Cómo se relacionan los módulos `main.py`, `library.py`, `book.py` y `user.py` para formar el sistema completo?
Respuesta: Siguen un diseño modular con separación de responsabilidades:
- `book.py` y `user.py`: Definen las estructuras de datos fundamentales (los "modelos").
- `library.py`: Actúa como el "controlador" que contiene la lógica de negocio. Importa las clases `Book` y `User` para gestionar las colecciones y las interacciones entre ellas (préstamos, devoluciones, etc.).
- `main.py`: Es el punto de entrada y la interfaz de usuario (la "vista"). Importa la clase `Library` y las demás para orquestar la aplicación, mostrando el menú, capturando la entrada del usuario y llamando a los métodos correspondientes de la biblioteca.