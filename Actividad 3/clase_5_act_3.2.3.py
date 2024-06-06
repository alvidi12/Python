"""
Creen un programa que solicite a los usuarios ingresar un texto. Luego, el programa debe analizar el texto y mostrar la frecuencia de cada palabra. Utilicen un diccionario para alma-cenar las palabras como claves y la frecuencia como valores.
"""
# Ejercicio 1: Frecuencia de Palabras en un Texto
texto = input("Ingrese un texto: ")
palabras = texto.split()

frecuencia_palabras = {}
for palabra in palabras:
    palabra = palabra.lower()  
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")
