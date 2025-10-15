1. Explica la diferencia entre una clase y un objeto en Python.
   Respuesta: Una clase es un molde o plantilla que define los atributos y métodos comunes de un tipo de dato. Un objeto es una instancia concreta de esa clase, con valores propios para sus atributos. Por ejemplo, `Time` es la clase, y `t1 = Time()` crea un objeto con su propio estado de hora, minutos, segundos y formato.

2. ¿Qué diferencia hay entre un atributo de clase y un atributo de instancia?
   Respuesta: Un atributo de clase es compartido por todos los objetos de esa clase, mientras que un atributo de instancia es propio de cada objeto. En el ejemplo, `time_count` es de clase (se incrementa cada vez que se crea un objeto), mientras que `hours`, `minutes` y `seconds` son de instancia (cada objeto tiene los suyos).

3. Explica la utilidad del método constructor `__init__` en una clase.
   Respuesta: El método `__init__` se ejecuta automáticamente al crear un objeto y se usa para inicializar sus atributos. Permite establecer un estado inicial válido sin necesidad de hacerlo manualmente después de la creación del objeto.

4. ¿Qué ventajas aporta el uso de métodos privados (doble guion bajo) en una clase?
   Respuesta: Los métodos privados ocultan la implementación interna de la clase y evitan que el usuario los use o modifique directamente. Esto refuerza el principio de encapsulamiento y reduce los errores al usar la clase de forma incorrecta.

5. Define qué es el polimorfismo y da un ejemplo aplicado a estructuras de datos o clases.
   Respuesta: El polimorfismo permite usar un mismo método con diferentes tipos de objetos. Por ejemplo, si varias clases implementan un método `get_time()`, se pueden tratar de forma genérica sin importar su tipo exacto, siempre que todas definan ese método.

6. Explica la diferencia entre una tupla, una lista y un diccionario en Python.
   Respuesta:

* Tupla: inmutable, ordenada, se usa para conjuntos de datos fijos.
* Lista: mutable, ordenada, permite añadir o eliminar elementos.
* Diccionario: colección de pares clave-valor, ideal para acceder rápidamente a datos mediante una clave.
  En la clase `Time`, se usa una tupla para los formatos válidos porque no deben cambiar.

7. ¿Qué es una estructura de datos y cómo se relaciona con las clases en programación orientada a objetos?
   Respuesta: Una estructura de datos es una forma organizada de almacenar y gestionar información. Las clases son una extensión de este concepto, ya que permiten crear estructuras de datos personalizadas que, además de contener información (atributos), también pueden incluir comportamiento (métodos). Esto facilita el modelado de entidades del mundo real en los programas.
