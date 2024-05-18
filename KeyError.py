#Error al acceder al diccionario y el tipo de dato no existe

try: 
    diccionario = {"a": 2, "b":3}
    valor = diccionario["c"]
except KeyError: print("no existe el dato en el diccionario")