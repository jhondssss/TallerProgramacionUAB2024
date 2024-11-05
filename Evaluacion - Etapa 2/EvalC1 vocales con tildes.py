
texto = "Hola, ¿cómo estás hoy?"
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
cont_vocales = 0
resultado = ""

for char in texto:
    if char in vocales:
        resultado += f"{char} "
        cont_vocales += 1

# resultado = resultado[:-2]  
print(f"Vocales encontradas: {resultado}")
print(f"Cantidad de vocales: {cont_vocales}")