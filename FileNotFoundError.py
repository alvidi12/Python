#Cuando el archivo no existe o la ruta esta mal escrita

try:
    archivo = open("archivo-que-no-existe.txt", "r")
except FileNotFoundError: print("no existe tal archivo")