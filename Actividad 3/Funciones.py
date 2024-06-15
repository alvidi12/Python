#CLASE PRIMERA PARTE - 11/06/24
#Función sin argumento y sin retorno
def saludo():
    """
    Imprime un saludo sin recibir argumeto ni retorno
    """
    print("Hola mundillo")
saludo()

#Función sin argumento y con retorno
def obtener_suma():
    num1= 5
    num2= 90
    return num1+num2
print(obtener_suma())

#Función con argumento y sin retorno
def escribir_archivito(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    print(f"contenido guardado en {nombre_archivo}")

#Agregamos los datos
nombre_archivo = input("ingrese el nombre del archivo")
contenido = """Estas cookies son necesarias para proporcionar funcionalidades básicas mientras navega por los sitios web IBM. 
Estas capacidades incluyen preferencias de cookies, equilibrio de carga, administración de sesiones, selección de idioma y proceso de pago"""
escribir_archivito(nombre_archivo,contenido)

#Función que recibe argumentos y devuelve un return
def leer_acrhivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            return contenido         
    except FileNotFoundError:
        return "El archivo no fue encontrado"
    
nombre_archivo= input("Ingrese el archivo a leer: ")
contenido_archivo = leer_acrhivo(nombre_archivo)
print(f"Contenido de {nombre_archivo}:\n{contenido_archivo}")

#Ejemplo función con argumento y retorno
def contar_palabra(contenido):
    """Contar las palabras totales"""
    palabras = contenido.split()
    return len(palabras)
numero_palabras = contar_palabra(contenido_archivo)
print(f"El archivo: {nombre_archivo} tiene {numero_palabras} palabras")

def contar_lineas(contenido):
    lineas = contenido.split("\n")
    return len(lineas)
numero_lineas = contar_lineas(contenido_archivo)
print(f"El archivo: {nombre_archivo} tiene {numero_lineas} lineas")

#Función que encuentre la cantidad de palabras que se repiten en una cadena
def buscar_palabra(contenido, palabra):
    return contenido.lower().split().count(palabra.lower())
palabra = input("Ingrese la palabra a encontrar: ")
apariciones = buscar_palabra(contenido, palabra)
print(f"La palabra {palabra} aparece {apariciones} veces en el archivo {nombre_archivo}")

#Esta función recibe una cantidad indeterminada de argumentos *args tuplas
def suma_multiple(*args):
    suma_total = 0
    print(type(args))
    for numero in args:
        suma_total += numero
    return suma_total

#Llamar a la función
resultado_multiple = suma_multiple(1,2,3,4,5,6,7,8,9,10)
print(f"La suma de 1,2,3,4,5,6,7,8,9,10 es: {resultado_multiple}")

#CLASE SEGUNDA PARTE - 13/06/24
#Función con **kwarg
def saludo_completo(**kwargs):
    saludo = "Hola "
    for clave, valor in kwargs.items():
        saludo += f"{valor}"
    saludo += "Bienvenido a la clase de funciónes 2 "
    print(saludo)
    print(type(kwargs))

#Llamada a la fx
saludo_completo(nombre="Andy ", apellido="Villarroel ")

#Función *args (tupla) y **kwargs (diccionario)
def informacion_completa(*tupla, **diccionario):
    print("Información recibida")
    for args in tupla:
        print(f"{args}")
    for clave, valor in diccionario.items():
        print(f"Clave: {clave}, Valor: {valor}")
informacion_completa(1,2,3,4,5,6,7,8,9, nombre="Andy", comuna="Puerto Montt")

#Función que recibe argumentos más complejas
def estadisticas(*args):
    suma_total = sum(args)
    promedio = suma_total/len(args)
    maximo = max(args)
    minimo = min(args)
    return suma_total, promedio, maximo, minimo

#Llamamos a la fx
suma_total, promedio, maximo, minimo = estadisticas(10,20,30,40,50)
print(f"Suma total: {suma_total}\nPromedio: {promedio}\nMáximo: {maximo}\nMínimo: {minimo}")

#Función recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
resultado_factorial = factorial(5)
print(f"El factor de 5 es: {resultado_factorial}")

#Función anidada
def operacion_anidada(a,b):
    def suma(numero1, numero2):
        return numero1 + numero2
    def multiplicar(numero1, numero2):
        return numero1*numero2
    total_suma = suma(a,b)
    total_multiplicacion = multiplicar(a,b)
    return total_suma, total_multiplicacion

total_suma, total_multiplicacion = operacion_anidada(10,20)
print(f"La suma de 10 + 20 es: {total_suma} y la multiplicacion de 10*20 es: {total_multiplicacion}")

#Ejemplo de una fx lambda
elevar_cuadrado = lambda X: X**2
lista_de_numeros = [1,2,3,4,5]
numeros_cuadrados = list(map(elevar_cuadrado, lista_de_numeros))
print(f"Los números {lista_de_numeros} al cuadrado son {numeros_cuadrados}")