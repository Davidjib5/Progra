# clases.py
from excepciones import ErrorBiblioteca

class Publicacion:
    def __init__(self, titulo, autor, anio):
        # Usamos los setters (propiedades) para asignar valores y validar
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    # --- Decoradores para Encapsulamiento (Titulo) ---
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor or len(valor.strip()) == 0:
            raise ErrorBiblioteca("El título no puede estar vacío.")
        self._titulo = valor  # Nota: usamos _titulo (atributo protegido)

    # --- Decoradores para Autor ---
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        if not valor or len(valor.strip()) == 0:
            raise ErrorBiblioteca("El autor no puede estar vacío.")
        self._autor = valor

    # --- Decoradores para Año ---
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ErrorBiblioteca("El año debe ser un entero positivo.")
        self._anio = valor

    def descripcion(self):
        """Método base para visualizar datos."""
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"


class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        # Llamada al constructor de la clase padre
        super().__init__(titulo, autor, anio)
        self.genero = genero

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        if not valor:
            raise ErrorBiblioteca("El género no puede estar vacío.")
        self._genero = valor

    # Sobrescritura de método (Polimorfismo)
    def descripcion(self):
        base_desc = super().descripcion()
        return f"[LIBRO] {base_desc}, Género: {self.genero}"


class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self.num_edicion = num_edicion

    @property
    def num_edicion(self):
        return self._num_edicion

    @num_edicion.setter
    def num_edicion(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ErrorBiblioteca("El número de edición debe ser mayor a 0.")
        self._num_edicion = valor

    # Sobrescritura de método (Polimorfismo)
    def descripcion(self):
        base_desc = super().descripcion()
        return f"[REVISTA] {base_desc}, Nº Edición: {self.num_edicion}"