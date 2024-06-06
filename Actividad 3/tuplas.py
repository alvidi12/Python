"""
Tuplas: 
Son estructuras de datos parecidaas a las listas pero con algunas diferencias.
son inmutables (No se pueden modificar).
Las tuplas se definen mediante parentesis.
Son una secuencia de elementos.
"""

#1.Definir una tupla
tupla_1 = (1,2,3,4,5)
#2.Definir una tupla
tupla_2 = 1,2,3,4,5,"holi"
#3.Definir una tupla
tupla_3 = tuple([1, "Chao", 333, True])
print(type(tupla_3))

#Acceder a a dato?
print(tupla_3[1])

#Rango dentros de las tuplas
print(tupla_3[1:3])

tupla_4 = (33,5,8,33,5,888,45,7,32,8,0,6,3443,6,5,6,3,5,6,5,7,8)

# funciones len, max, min, sum. count, index
#número máximo de mi tupla_4 print...llamar a la tupla...
print(max(tupla_4))

#Contar las posiciones de mi tupla
print(len(tupla_4))

# sumar todos los números de mi tupla 
print(sum(tupla_4))

#Metodos y tuplas count, index
#Cuantos numeros 5 tiene la tupla.
print(tupla_4.count(5))

#posición exacta del número 888
print(tupla_4.index(888))

#desempaquetado de tuplas
tupla_5 = (1,2,3)
a,b,c = tupla_5
print(a)
print(b)
print(c)