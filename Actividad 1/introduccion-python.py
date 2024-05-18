# commit de python 1.
"""
Comentarios de varias lineas
"Muy util para cargar comentarios en un documento al momento de exportarlo".
Qué es una variable? : Es un espacio de memoria reservado para almacenar datos que pueden cambiar en el transcurso del programa.
Python es una lenguaje de programación dinámico, no es necesario declarar explícitamente el tipo de variable antes de utilizarla.
"""
#Variables de python:
#Deben contener letras, números o guiones bajos.
#Deben comenzar con una letra.
#Case sensitive (sensible a las letras mayúsculas).

variable = 1
Variable = 1

#No se pueden utilizar palabras reservadas para definir variables.
none = 1

"""
False, None, True, and, assert, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, try, while, with, as y yield.
"""

#Tipos de datos:
entero = 2
decimalFloat = 1.5
cadenaTexto = "soy cadena"

suma = 2+2
resta = 2-2
multiplicacion = 2*2
division = 2/2

#Imprimir datos:
print (suma)
print (division, resta)

mensaje = "hola"
nombre = "extraño"
print(mensaje, nombre)

#Concadenar variable + texto.
print(mensaje + "texto extra" + nombre)

#Booleano
edad = 18
esEstudiante = True
estaTrabajando = False

#Operación lógica con booleanos.
esMayorDeEdad = edad >= 18
puedeVotar = esMayorDeEdad and estaTrabajando
print (esMayorDeEdad)
print(puedeVotar)

#Listas: son colecciones de datos ordenados y modificables. []
numero = [1,2,3,4,5,6,7,8,9,0]
nombres = ["Don","Campo","Sir"]
mixta = [1, "Don", True, 1.4]

print(numero)
print(numero[6])

print(nombre)

print(mixta)
print(mixta[-1])

#Tuplas: son colecciones de datos ordenados e inmutables. ()
coordenadas = (10,20)
meses = ("Enero", "Febrero", "Marzo")

print(meses)