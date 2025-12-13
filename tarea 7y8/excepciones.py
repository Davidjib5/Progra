# excepciones.py

class ErrorBiblioteca(Exception):
    """Excepción base para errores de la biblioteca."""
    def __init__(self, mensaje="Error en la biblioteca"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorArchivo(ErrorBiblioteca):
    """Excepción para errores relacionados con ficheros."""
    def __init__(self, mensaje="Error al procesar el archivo"):
        super().__init__(mensaje)