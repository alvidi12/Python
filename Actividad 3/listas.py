"""
Tipos de datos que permiten almacenar cualquier tipo de dato.
-Mantienen el orden con el que fueron definidas.
-Es que se pueden definir.
-Son mutables: pueden ser modificadas.
-Son dinamicas: que se pueden añadir y modificar elementos.
"""

#Definamos las listas []
lista = [1,2,3,4,5,6,7,8,9]
lista_variada = [123, "Hola", 3.4, True]

#Imprimir un dato especifico
print(lista_variada[3])
print(lista_variada[-1])

#Cambiar un elemento
lista_variada[3] = False
print(lista_variada)

#Eliminar un elemento
del lista_variada[3]
print(lista_variada)

#Agregar un rango a mi lista
lista[9:12] = [10,11,12]
print(lista)

#Asignar una lista a variables.
lista_numeros = [1,2,3]
a,b,c = lista_numeros
#lista_letras = ["a", "b", "c"]
print(a)
print(b)
print(c)

#Iterar una lista
#Lista = [1,2,3,4,5,6,7,8,9]
for i in lista:
    print(i)

#Imprimir la posicion de la lista
for index, l in enumerate(lista):
    print(f"indice: {index}, numero de lista: {l}")

#Unir 2 listas
lista1= [2,5,9]
lista2= ["Jazz", "Rock", "Rappi"]
#Unimos las listas
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)

#Agregar un elemento a la lista
lista.append(14)
print(lista)

#Ordenar una lista menor a mayor
lista_desordenada = [6,7,9,2,3,5,0,9,1]
lista_desordenada.sort()
print(lista_desordenada)

#Ordenar una lista mayor a menor
lista_desordenada.sort(reverse=True)
print(lista_desordenada)

#Eliminar el ultimo elemento
lista_nueva = [1,2,3]
lista_nueva.pop()
print(lista_nueva)

#Remover un elemento
lista_nueva[1]
