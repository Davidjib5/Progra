    Pregunta: En la clase Empleado, dentro del __init__, llamamos a super().__init__(nombre, edad, nacio). ¿Qué pasaría si omitimos esa línea?

        Respuesta: Los atributos de la clase base (_nombre, _edad, _nacio) no se inicializarían. El objeto Empleado se crearía, pero al intentar acceder a self.nombre (o self._nombre), Python lanzaría un error (AttributeError) porque esas variables nunca se definieron en el contexto de la nueva instancia.

    Pregunta: En RegistroDiario implementamos el método __getitem__. ¿Qué nos permite hacer esto exactamente en el código principal (main.py)?

        Respuesta: Nos permite tratar al objeto registro como si fuera una lista o un array. Gracias a esto, podemos escribir persona = registro[idx] en lugar de tener que crear un método explícito como registro.get_persona_at(idx).

    Pregunta: Fíjate en el método __add__ de RegistroDiario. ¿Por qué creamos una instancia nuevo_registro dentro del método en lugar de modificar self._personas directamente?

        Respuesta: Para mantener la inmutabilidad de los operandos. Cuando sumas a + b, esperas obtener un tercer resultado c, no que a cambie. Si modificáramos self, estaríamos alterando el registro original, lo cual es un efecto secundario no deseado en una operación de suma.

    Pregunta: En la clase Cliente, definimos __eq__. Si no lo hubiéramos definido y hacemos cliente1 == cliente2 (teniendo ambos los mismos datos), ¿qué resultado daría?

        Respuesta: Daría False. Por defecto, en Python, la comparación == entre objetos comprueba si son la misma instancia en memoria (identidad). Al sobrescribir __eq__, cambiamos el comportamiento para comparar por valor (contenido de los atributos).

    Pregunta: En la función visualizar_registro, recorremos la lista y llamamos a p.Visualizar(). ¿Cómo sabe Python si debe imprimir los datos de un Cliente (con DNI) o de un Empleado (con Categoría)?

        Respuesta: Esto es el Polimorfismo. Python determina en tiempo de ejecución el tipo de la variable p. Si p apunta a un objeto Empleado, ejecuta el Visualizar de Empleado; si apunta a Cliente, ejecuta el de Cliente.

    Pregunta: En agregar_persona usamos if isinstance(persona, (Empleado, Cliente)):. ¿Qué principio de la Programación Orientada a Objetos estamos reforzando aquí?

        Respuesta: Estamos reforzando la seguridad de tipos (aunque Python es de tipado dinámico). Nos aseguramos de que la lista _personas sea homogénea en cuanto a la jerarquía de clases (solo contiene descendientes de Ficha), garantizando que luego podremos llamar a métodos como Visualizar() sin errores.

    Pregunta: En los métodos setter (por ejemplo @edad.setter), simplemente asignamos el valor (self._edad = val). ¿Cuál es la ventaja de tener este método si no estamos validando nada (como que la edad sea positiva)?

        Respuesta: La ventaja es la extensibilidad y mantenibilidad. Si mañana te piden que la edad no pueda ser negativa, solo tienes que añadir un if val < 0: raise ValueError dentro del setter. No tendrías que cambiar ninguna línea de código en el main.py ni en otras partes donde se asigne la edad, ya que la interfaz de uso sigue siendo objeto.edad = 5.


Puntos Clave y Explicación Adicionales

    Herencia (class Empleado(Ficha)):

        Empleado y Cliente heredan de Ficha.

        super().__init__(...): Es fundamental en los constructores de las clases hijas para asegurar que los atributos de la clase base (_nombre, _edad, _nacio) se inicialicen correctamente antes de añadir los específicos (_categoria, _dni, etc.).

    Polimorfismo:

        Fíjate en el método Visualizar(). Está definido en Ficha pero sobrescrito en Empleado y Cliente.

        En RegistroDiario.visualizar_registro(), iteramos sobre una lista mixta. Al llamar a p.Visualizar(), Python determina automáticamente qué versión del método ejecutar dependiendo de si p es un Empleado o un Cliente en tiempo de ejecución.

    Encapsulamiento y Decoradores:

        Usamos _variable (con un guion bajo) para indicar que son atributos protegidos.

        Usamos @property para leer el valor (getter) y @nombre.setter para modificarlo. Esto permite controlar el acceso o validar datos en el futuro sin cambiar la interfaz de la clase.

    Sobrecarga de Operadores (Métodos Mágicos):

        __eq__ (en Cliente): Permite usar cliente1 == cliente2. Python llamará automáticamente a este método para comparar sus atributos.

        __getitem__ (en RegistroDiario): Permite usar la sintaxis registro[0]. Hace que el objeto se comporte como una lista.

        __add__ (en RegistroDiario): Permite usar registro1 + registro2. Crea una nueva instancia de RegistroDiario y suma las listas internas de personas.