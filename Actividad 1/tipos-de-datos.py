#Números complejos
numeroComplejo = 5j #Crea un número con parte real 5 la parte imaginaria J

#Datos de tipo rango o range
#Crea un objeto con el rango desde cero hasta 9
rango = range(9)

#Mostrar el rango
print(rango)

#Mostrar tipo de dato
print(type(rango))

"""
frozenset: Es un tipo de colección similar a un set() regular, con la diferencia que los datos no se pueden modificar, eliminar o actualizar.
"""

frutas = frozenset({"Arándanos", "Manzanas", "Kiwi"}) #Crea un frozenset.
print(frutas)
print(type(frutas))

"""
Bytes: Es un tipo de dato inmutable desde 0 a 255.
Se puede crear a partir de una cadena de carácteres, un lista, enteros o un objeto byte existente.
Se utiliza principalmente para almacenar dato binarios como archivos o datos de red.
"""

"""
¿qué es utf-8?
UTF-8 es un formato de codificación de caracteres Unicode e ISO 10646 que utiliza símbolos de longitud variable.
"""

#Crear un objeto byte a partir de una cadena de caracteres.
#Crear un objeto byte a partir de una cadena utilizando la codificación utf-8.
tipoByte = bytes("Hola", "utf-8")
print(tipoByte)
print(type(tipoByte))

#Crear un objeto bytes a partir de números enteros
objetoByte = bytes([72,79,108,97])
print(objetoByte)
print(type(objetoByte))

"""
Abecedario en Byte
A: 65
B: 66
C: 67
D: 68
E: 69
F: 70
G: 71
H: 72
I: 73
J: 74
K: 75
L: 76
M: 77
N: 78
O: 79
P: 80
Q: 81
R: 82
S: 83
T: 84
U: 85
V: 86
W: 87
X: 88
Y: 89
Z: 90

a: 97
b: 98
c: 99
d: 100
e: 101
f: 102
g: 103
h: 104
i: 105
j: 106
k: 107
l: 108
m: 109
n: 110
o: 111
p: 112
q: 113
r: 114
s: 115
t: 116
u: 117
v: 118
w: 119
x: 120
y: 121
z: 122
"""

"""
ByteArray: Un tipo de dato mutable, lo que significa que su contenido se puede modificar.
0-255
Se utiliza cuando tenemos que manipular datos de forma dinámica como en lecturay escritura de flujo de datos.
"""

#Crea un bytearray()
byteArray = bytearray("Holass", "utf-8")
print(byteArray)
print(type(byteArray))

byteArray[0] = 104 # en [0] debe ir la posicion del caracter del texto anterior que desea modificar.
print(byteArray)

byteArray[5] = 104
print(byteArray)

#Memoryview: Es un tipo de dato que nos permite acceder y manipular de forma eficiente la memoria adyacente de un objeto
#Crear una vista de memoria.

vista = memoryview(byteArray)
print(vista)

#Imprimir el primer elemento del array
print(vista[3])

#Modificar un elemento array.
vista[0] = 74
print(vista[0])
print(byteArray)

#None: Es un tipo de dato que representa la ausencia de valor.
variableNone = None
print(variableNone)

#Funciones def
def saludar(nombre):
    return "!Hola¡ " + nombre + "insecto"

#Mensaje de saludo personalizado
mensajeSaludo = saludar("Estudiante ")
print(mensajeSaludo)

"""
Crear 2 archivos distintos nuevos .py
1. Solicitar datos al usuario de temperatura y el programa deberá convertir de Farenheit a Celcius e  imprimir un mensaje por consola.

2.Calculadora con funciones básicas + , - , * , / utilizando las funciones de Python def. 

Al terminar las suben a su repositorio en github "Acumulativas-modulo-2"
"""