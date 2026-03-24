texto = str(input("Ingrese un texto: ")).lower()

def eliminar_signos(texto):
    signos = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    texto_sin_signos = texto
    for signos in texto_sin_signos:
        texto_sin_signos = texto_sin_signos.replace(signos, "").lower()
        continue
    return texto_sin_signos
def contar_palabras(texto, ignoradas):
    texto_sin_signos = eliminar_signos(texto)
    palabras = texto_sin_signos.split()
    palabras_filtradas = [p for p in palabras if p not in ignoradas]
    return palabras_filtradas, {p: palabras.count(p) for p in set(palabras_filtradas)}

texto_sin_signos = eliminar_signos(texto)
palabras = texto_sin_signos.split()
frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1
def top_n(frecuencias, n=5):

    items = list(frecuencias.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]

def mostrar_resultados(lista_filtrada, frecuencias, n=5):
    total_palabras = len(lista_filtrada)
    palabras_unicas = len(frecuencias)
    print(f"\nCantidad total de palabras (sin contar palabras ignoradas): {total_palabras}")
    print(f"Cantidad de palabras únicas: {palabras_unicas}\n")
    print(f"Top {n} palabras más repetidas:\n")
    for palabra, freq in top_n(frecuencias, n):
        print(f"{palabra} -> {freq}")

def main():
    ignoradas = {"el", "la", "de", "y", "a", "un", "una"}
    texto = input("Ingresa un texto: ")
    lista_filtrada, frecuencias = contar_palabras(texto, ignoradas)
    mostrar_resultados(lista_filtrada, frecuencias, n=5)

if __name__ == "__main__":
    main()

