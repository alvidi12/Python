#Importar las librerías necesarias
import csv #Excel separado por comas
import json

#Crear un archivo de texto .txt
def crear_archivo_texto(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"archivo TXT: {nombre_archivo} creado exitosamente")

#Funcion para crear archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"archivo CSV: {nombre_archivo} creado exitosamente")

#Crear un JSON
def crear_archivo_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print(f"archivo json: {nombre_archivo} creado exitosamente")

#leer archivo txt
def leer_archivo_txt(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

#Leer archivo csv
def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return list(csv.reader(archivo))

#Leer archivo json
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)

#Agregar texto a un txt existente
def agregar_contenido_txt(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(contenido)
    print(f"contenido agregado en TXT: {nombre_archivo} exitosamente")

contenido_txt = "Este es un texto de ejemplo"
crear_archivo_texto('ejemplo.txt', contenido_txt)

#Datos csv
datos_csv = [
    ['nombre', 'edad', 'comuna'],
    ['Eduardo', 33, 'Puerto Montt'],
    ['Antonella', 18, 'Puerto Montt'],
    ['Jhon', 24, 'Puerta Sur']
]
crear_archivo_csv('ejemplo.csv', datos_csv)

#Datos json
datos_json= {
    'nombre': 'marcelo',
    'edad': 37,
    'comuna': 'llanquihue',
    'habilidades': ['python', 'HTML', 'CSS']
}
crear_archivo_json('ejemplo.json', datos_json)

print(leer_archivo_txt('ejemplo.txt'))

#Mostrar y leer el archivo csv
for fila in leer_archivo_csv('ejemplo.csv'):
    print(fila)

#Mostrar y leer el archivo json
print(json.dumps(leer_archivo_json('ejemplo.json'), indent=4))
