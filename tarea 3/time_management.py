import re

class Time:
    """Clase que representa una hora con formato AM/PM o 24 horas."""

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0  # Contador de objetos creados

    def __init__(self):
        """Inicializa los atributos a 0 y formato vacío."""
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HOURS"
        Time.time_count += 1

    def __assign_format(self, pszFormat):
        """Verifica y asigna el formato (AM, PM o 24 HOURS)."""
        pszFormat = pszFormat.strip().upper()
        if pszFormat in Time.TIME_FORMATS:
            self.format = pszFormat
            return True
        return False

    def __is_24hour_format(self):
        """Devuelve True si el formato es 24 HORAS."""
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        """Verifica que la hora sea válida según el formato."""
        if self.__is_24hour_format():
            return (0 <= self.hours <= 23) and (0 <= self.minutes <= 59) and (0 <= self.seconds <= 59)
        else:
            return (1 <= self.hours <= 12) and (0 <= self.minutes <= 59) and (0 <= self.seconds <= 59)

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        """Asigna una hora si todos los datos son válidos."""
        if not self.__assign_format(pszFormato):
            print("❌ Formato no válido.")
            return False

        self.hours = nHoras
        self.minutes = nMinutos
        self.seconds = nSegundos

        if not self._is_valid_time():
            print("❌ Hora no válida según el formato.")
            return False

        return True

    def get_time(self):
        """Devuelve la hora en formato de cadena."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """Crea un objeto Time a partir de una cadena."""
        pattern = r"^(\d{1,2}):(\d{2}):(\d{2})\s*(AM|PM|24 HOURS)$"
        match = re.match(pattern, time_string.strip(), re.IGNORECASE)
        if not match:
            print("❌ Formato de cadena incorrecto. Ejemplo: '14:30:00 24 HOURS'")
            return None

        hours, minutes, seconds, fmt = match.groups()
        new_time = cls()
        if new_time.set_time(int(hours), int(minutes), int(seconds), fmt):
            return new_time
        else:
            print("❌ Error al crear la hora desde la cadena.")
            return None

    @staticmethod
    def is_valid_format(time_format):
        """Comprueba si el formato es válido."""
        return time_format.strip().upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """Devuelve el número total de objetos Time creados."""
        return cls.time_count


# ----------- FUNCIÓN AUXILIAR -----------
def show_time(time_obj):
    """Devuelve la hora con formato legible."""
    return f"Hora actual: {time_obj.get_time()}"


# ----------- MENÚ PRINCIPAL -------------
def main():
    current_time = Time()

    while True:
        print("\n===== MENÚ DE GESTIÓN DE HORA =====")
        print("1. Introducir nueva hora")
        print("2. Visualizar hora actual")
        print("3. Crear hora desde cadena (HH:MM:SS FORMATO)")
        print("4. Terminar")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            try:
                h = int(input("Horas: "))
                m = int(input("Minutos: "))
                s = int(input("Segundos: "))
                fmt = input("Formato (AM, PM o 24 HOURS): ")
                if current_time.set_time(h, m, s, fmt):
                    print("✅ Hora actualizada correctamente.")
            except ValueError:
                print("❌ Entrada inválida. Usa solo números.")
        elif choice == "2":
            print(show_time(current_time))
        elif choice == "3":
            cadena = input("Introduce la cadena de hora (HH:MM:SS FORMATO): ")
            nueva = Time.from_string(cadena)
            if nueva:
                current_time = nueva
                print("✅ Hora creada correctamente.")
        elif choice == "4":
            print("👋 Fin del programa.")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    main()
