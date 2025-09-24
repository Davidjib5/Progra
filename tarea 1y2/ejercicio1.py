def process_text(text="This is a default text with Python and amazing words.",
                 words_to_replace=["python", "amazing"]):
    # Convertir a minúsculas y eliminar espacios
    text = text.lower().strip()

    # Separar el texto en palabras
    word_list = text.split()
    replaced_count = 0

    # Procesar cada palabra
    for i in range(len(word_list)):
        if word_list[i] in words_to_replace:
            word_list[i] = '*' * len(word_list[i])
            replaced_count += 1

    # Reconstruir el texto
    processed_text = ' '.join(word_list)
    
    return processed_text, replaced_count

# Función principal
def main():
    result_text, count = process_text()
    print(f"Processed text: \"{result_text}\"")
    print(f"Palabras remplazadas: {count}")

# Llamada a la función principal
main()
