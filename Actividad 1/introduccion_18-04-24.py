#Los Conjunto de datos desordenados y no indexados de elementos unicos. Se define utilizando llaves {} o la funcion ().

#Conjunto de numeros
numerosPrimos = {2,3,5,7,11}

#Conjunto de letras
lenguaje = set("Python3")

#Agregar elementos a un conjunto
numerosPrimos.add(13)   
print (numerosPrimos)

#Eliminar datos de un conjunto.
lenguaje.remove("3")
print (lenguaje)

#Diccionarios: son colecciones de datos pares clave: valor {}
alumno ={
    "Nombre" : "ElJuan",
    "Edad": 30,
    "Beca": True,
    "Ciudad": "Puerto Puerto",
    "Provincia": "Yankigue",
    "Comuna": "Puerto Moon",
}
print(alumno)

#Imprimir dato especifico de un diccionario.
print(alumno["Beca"])
print(alumno["Edad"])

#Modificar un dato especifico de un diccionario.
alumno["Edad"] = 50
print(alumno)

#Agregar un nuevo clave: valor.
alumno["Altura"] = 1.20
alumno["Nombre"] = "Miguelito"
print(alumno)

#Como saber de que tipo es una variable typeof.
print (type (numerosPrimos))
print (type (alumno))
print (type (lenguaje))

#Como obtener un dato del usuario.
datoUsuario = input ("Ingrese un numero")
print(datoUsuario)
print (type (datoUsuario))