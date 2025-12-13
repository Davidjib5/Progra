    Pregunta: En clases.py, dentro de @titulo.setter, usamos self._titulo = valor. ¿Por qué usamos el guion bajo (_titulo) y no self.titulo = valor?

        Respuesta: Si usamos self.titulo = valor dentro del propio setter, estaríamos llamando al setter recursivamente de forma infinita (RecursionError). Usamos _titulo para almacenar el dato real en un atributo protegido interno.

    Pregunta: En el método descripcion() de Libro, aparece super().descripcion(). ¿Qué función cumple exactamente?

        Respuesta: Invoca al método descripcion() de la clase padre (Publicacion). Esto permite reutilizar el código que ya formatea el título, autor y año, para luego solo concatenar el género específico del libro. Promueve la reutilización de código (DRY).

    Pregunta: En main.py, opción 2, recorremos la lista biblioteca e imprimimos pub.descripcion(). ¿Cómo sabe Python si debe ejecutar el método de Libro o el de Revista?

        Respuesta: Esto es Polimorfismo dinámico. Aunque la variable pub sea genérica en el bucle, Python mira el tipo real del objeto en tiempo de ejecución (runtime) y ejecuta la versión del método correspondiente a esa clase específica.

    Pregunta: En Utils.py, utilizamos pickle.dump y pickle.load. ¿Por qué es obligatorio abrir el archivo con los modos 'wb' y 'rb' en lugar de 'w' y 'r'?

        Respuesta: pickle convierte objetos de Python en un flujo de bytes (binario), no en texto. Si abrimos el archivo en modo texto (w/r), Python intentará codificar/decodificar caracteres (como UTF-8), lo cual corromperá los datos binarios de pickle.

    Pregunta: ¿Qué ventaja tiene crear la clase ErrorArchivo heredando de ErrorBiblioteca en lugar de heredar directamente de Exception?

        Respuesta: Permite agrupar errores. En el main.py o en un nivel superior, podemos poner un except ErrorBiblioteca: y capturará tanto errores de validación de datos como errores de archivo, permitiendo una gestión de errores jerárquica y más limpia.

    Pregunta: Si intentamos crear un objeto Revista con un año negativo, el programa no se detiene abruptamente. ¿Qué mecanismo del código lo impide?

        Respuesta: El setter de anio lanza (raise) una excepción ErrorBiblioteca. En el main.py, opción 1, todo el bloque de creación está dentro de un try...except ErrorBiblioteca. Al capturar la excepción, imprimimos el mensaje amigable y el bucle while del menú continúa.

    Pregunta: En Utils.py, usamos with open(...) as f:. Si ocurre un error justo mientras se están escribiendo datos (antes de acabar), ¿el archivo queda abierto?

        Respuesta: No. La estructura with es un Context Manager. Garantiza que, pase lo que pase (incluso si hay una excepción o el programa falla dentro del bloque), se llamará automáticamente al método interno __exit__ que cierra el archivo correctamente, evitando corrupción o bloqueos de recursos.