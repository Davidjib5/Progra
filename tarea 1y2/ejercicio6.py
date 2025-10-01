import re
from datetime import datetime

# Texto original del informe
informe = """Informe clínico de Urgencias
Nombre: Juan Pérez López
Género: Hombre
Fecha de nacimiento: 12/05/1980
Motivo de consulta: dolor abdominal
12/05/2023 Dr. Ramírez
Tratamiento: reposo y analgésicos"""

def anonimizar_informe(texto):
    # Regex para fechas (dd/mm/aaaa o d/m/aaaa)
    patron_fecha = re.compile(r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b')

    # Buscar fecha de nacimiento
    nacimiento_match = re.search(r'Fecha de nacimiento: (\d{1,2}/\d{1,2}/\d{4})', texto)
    edad = None

    if nacimiento_match:
        fecha_nacimiento_str = nacimiento_match.group(1)
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y')

        # Buscar la fecha de ingreso más cercana (asumimos primera fecha distinta a nacimiento)
        fechas_encontradas = patron_fecha.findall(texto)
        for dia, mes, anio in fechas_encontradas:
            fecha_actual_str = f"{dia}/{mes}/{anio}"
            if fecha_actual_str != fecha_nacimiento_str:
                fecha_ingreso = datetime.strptime(fecha_actual_str, '%d/%m/%Y')
                edad = fecha_ingreso.year - fecha_nacimiento.year - (
                    (fecha_ingreso.month, fecha_ingreso.day) < (fecha_nacimiento.month, fecha_nacimiento.day)
                )
                break

    # Reemplazar línea del paciente
    texto = re.sub(r'^Nombre: .+', 'Nombre: PACIENTE', texto, flags=re.MULTILINE)

    # Reemplazar nombres de doctores (líneas que contienen Dr. o Dra.)
    texto = re.sub(r'(Dr\.|Dra\.)\s+[A-Za-zÁÉÍÓÚáéíóúñÑ]+', 'MEDICO', texto)

    # Eliminar la línea de "Fecha de nacimiento" y agregar "Edad: X"
    if edad is not None:
        texto = re.sub(r'^Fecha de nacimiento: .+', f'Edad: {edad}', texto, flags=re.MULTILINE)

    # Reemplazar todas las fechas por "FECHA"
    texto = patron_fecha.sub("FECHA", texto)

    return texto

# Procesar el informe
informe_anonimizado = anonimizar_informe(informe)

# Mostrar resultado
print(informe_anonimizado)
