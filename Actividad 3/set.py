"""
Set: 
-se crean utilizando {}.
-usando la funcion set().
-agrupar conjunto de datos.
-no se pueden acceder a los datos   por un indice, solo por el valor.
-Se pueden iterar.
-los datos no son ordenados.
"""
#1ra manera
set1 = {10,20,30,40,50}
#2da manera
set2 = ([60,70,80,90,100])

#iterar sobre un set

for indice in set1:
    print(indice)

"""
Agregar y eliminar elementos en set()
add(): agrega un solo elemento.
update(): agregamos multiples elementos.
remove(): eliminamos un elemento especifico. (genera un error si no existe)
dicard(): eliminamos un elemento especifico. (no genera error si no exite)
clear(): vacia un set{...}
"""

#Crear un diccionario con set() y agregar un 
# elemento con add()

set3 = set([1,2,3,4,5])
set3.add(6)
print(set3)

#update()
set3.update([1,2,3,4,5,60])
print(set3)

#remover un elemento
set3.remove(60)
print(set3)

#Discard()
set3.discard(90)
print(set3)

#ejemplo de .pop() = eliminar un elemento aleatorio
elemento = set3.pop()
print(f"elemento eliminado: {elemento}")
print(set3)

#Vaciar el diccionario con clear()
set3.clear()
print(set3)

"""
Operaciones de conjunto:
union(): retorna la union de 2 set o conjunto.
intersection(): retorna la interseccion de 2 sets.
difference(): retorna la diferencia de 2 sets.
symetric_difference(): retorna la diferencia simetrica entre 2 sets.
Operadores de conjunto:
| unión
& para la inteseccion
- para la diferencia
^ para la diferencia simétrica
"""
print("")
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

#union de 2 sets nombre_nuevo_Set=set1.union(set2)
nuevo_Set = set_a.union(set_b)
print(nuevo_Set)

#interseccion .intersection()
inter= set_a.intersection(set_b)
print(inter)

#diference()
diff = set_a.difference(set_b)
print(diff)

#diferencia .difference()
diff_sym = set_a.symmetric_difference(set_b)
print(f"Diferencia simetrica: {diff_sym}")

#Operador |
print("")
op1= set_a|set_b
print(op1)

#Operador &
op2 = set_a&set_b
print(op2)

#Operador -
op3 = set_a-set_b
print(op3)

#Operador ^
op4 = set_a^set_b
print(op4)

#Copiar un set con copy()
setcopia= set_a.copy()
print(setcopia)

""""
Principales métodos
.copy()
isdisjoint(): Retorna  True si entre dos sets no hay elementos en común.
issubset()Retorna un si si es un sub conjunto de otro set
"""
set_h= {1,2,3}
set_i= {2,3,4}
set_j= {1,2,3,4,5}
print("")

# Verificar si no tienen elementos en común. isdisjoint()

print (set_h.isdisjoint(set_i)) #Devuelve un False porque hay valores que coinciden.