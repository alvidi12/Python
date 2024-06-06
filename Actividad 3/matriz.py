"""
Objetivos: 
-Comprender que es una matriz y como se utiliza en python.
-Diferenciar entre una matriz unidimensional, bidimensional y multidimensional.

Definición de una matriz: Es una estructura de datos que puede tener multiples dimensiones. 
"""
#Matriz unidimensional, pueden ser en orden vertical y horizontal
matriz_1d = [1,2,3,4,5,6]
#Acceder a un dato especifico
dato_especifico = matriz_1d[0]
#Actualizar un dato especifico
matriz_1d[0]= 100
print(matriz_1d)

#Agregar un elemento a mi matriz con .append()
matriz_1d.append(23)
print(matriz_1d)

#Eliminar un alemento con .remove()
matriz_1d.remove(3)
print(matriz_1d)
matriz_desordenada= [1,4,56,7,4,3,2,99,100,2333,4,0,]

#Ordenar esta matriz .sort() menor a mayor .sort(reverse=True)
matriz_desordenada.sort()
print(matriz_desordenada)
matriz_desordenada.sort(reverse=True)
print(matriz_desordenada)

#Matriz bidireccional: es una lista de listas (lista anidada dentro de otra lista).
matriz_2d = [
    [1,2,3], #0
    [4,5,6] #1
]
#Acceder a un elemento especifico: 6 [Fila][Columna]
resultado_matriz_2d = matriz_2d[1][1]
print(resultado_matriz_2d)

#Modificar el numero 6 por un numero 60
matriz_2d[1][2] = 60
print(matriz_2d)

#Recorrer una matriz bidimensional con el ciclo 1er for: recorre filas; 2do for: recorre columnas.
for i in matriz_2d:
    for l in i:
        print(l)
#Matriz multidimensionales: es una matriz que extiende su contenido a multiples dimensiones.
matriz_3d = [
    [#0
       [1,2,3,4,5], #0
       [6,7,8,8,9,10] #1
    ],
    [ #1
    [11,12,13,14], #0
    [15,16,17,18] #1
   ]
]
#Acceder a un elemento especifico de m3d [][][]
resultado_matriz_3d = matriz_3d[0][1][3]
print(resultado_matriz_3d)

#Modificar el numero 13 por el numero 133
matriz_3d[1][0][2] = 133
print(matriz_3d)

#Quiero recorrer mi matriz con un ciclo x3:
for i in matriz_3d:
    for l in i:
        for m in i:
            print(m)