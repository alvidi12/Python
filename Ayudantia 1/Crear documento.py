#Crear documento
import os # llama al sistema operativo
ruta_archivo = "nuevo_documento.txt"
contenido = "Este es el nuevo contenido del documento.\n ¡Creado con código Python!"

with open(ruta_archivo, "w")as archivo:
    archivo.write(contenido)

    print("Archivo en directorio actual: ")
    print(os.listdir(".")) # crea lista de los datos separados por un "."

    with open(ruta_archivo, "r") as archivo:
        contenido_leido = archivo.read() #Llama a leer un archivo seleccionado (.txt)

        print(f"\nContenido_leido = acrhivo:\n{contenido_leido}")
