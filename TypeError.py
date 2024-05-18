#Cuando el tipo de dato no es compatible

try:
    resultado = 5 + "10"
except TypeError: print("Tipo de dato no compatible")