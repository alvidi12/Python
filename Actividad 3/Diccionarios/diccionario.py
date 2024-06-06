"""
Diccionario: es un conjunto de datos estructurados mediante "clave": valor se define con {}.
Las claves pueden ser textos, numeros y cadenas.
Los valores pueden ser cualquier tipo de datos.
"""

#1ra manera
diccionario_autos = {
    "marca" : "Toyota",
    "modelo" : "Yaris",
    "año" : 2020
}
#2da manera
diccionario_alumno = dict(nombre="Miguel", apellido="Perez", edad=30)
print(type(diccionario_alumno))
print(type(diccionario_autos))

#Actualizar un elemento: llamo a mi diccionario ["clave"]= valor
diccionario_autos["año"]=2022
print(diccionario_autos)

#actualizar con .update: nombre diccionario.update({"clave": dato a actualizar})

diccionario_alumno.update({"nombre":"juan"})
print(diccionario_alumno)

"""
Elinmiar elementos
del
pop() elimina el último elemento
popitem() elimina el último par clave: valor
clear() vacia todo el diccionario
"""
#pop
diccionario_autos.pop("año")
print(diccionario_autos)
#popitem
diccionario_autos.popitem()
print(diccionario_autos)
#clear
diccionario_autos.clear()
print(diccionario_autos)

"""
len() cuenta
str() retorna una representación del diccionario en cadena
keys() claves 
values() valor
item() una vista de todos los pares clave valor
copy() realiza una copia del diccionario
"""
diccionario_autos = {
    "marca" : "Toyota",
    "modelo" : "Yaris",
    "año" : 2020
}

#len()
print(len(diccionario_autos))

#str()
print(str(diccionario_autos))

#keys()
print(diccionario_autos.keys())

#values()
print(diccionario_autos.values())

#items
print(diccionario_autos.items())

#Copiar un diccionario nombre_new_dict = diccinario.copy()
print("")

diccionario_autos_copia = diccionario_autos.copy()
print(diccionario_autos_copia)

#Iterar sobre las claves dor indice in diccionario:
#print()

for key in diccionario_autos_copia:
    print(key)

#Iterar sobre los valores .values()

for value in diccionario_autos_copia.values():
    print(value)

#Iterar sobre clave valor for indice1, indice in diccionario.items():

for value, key in diccionario_autos_copia.items():
    print(value, key)