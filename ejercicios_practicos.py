# 1)
#   Calculadora de IMC: Crea un programa que solicite al usuario su peso en kilogramos y su altura en metros. 
#   IMC =peso / (altura ** 2). Imprime el resultado del IMC con dos decimales.

altura = float(input("Ingrese su altura en formato 1.50: "))
peso =  float(input("Ingrese su peso en formato 50: "))
imc = peso / altura **2

print(f"Tu imc es de: {imc:.2f}") 
# a la variable imc se le agrega un .2 para especificar que imprima 2 decimales despues del punto, y f para decir que es un flotante.

#2)
#   Inversor de cadenas: Escribe un programa que pida al usuario una cadena de texto y luego imprima la cadena invertida.

"""
OP1:

def reverse(string):
    string = "".join(reversed(string))
    return string

string = input("Escriba algo: ")
print(f"Original: {string}")
print(f"Invertida: {reverse(string)}")

"""

texto = input("Ingrese algo para invertir: ")
#funció slicing: [entrada:fin:paso]
cadenaInvertida = texto[::-1]
print(f"La cadena invertida es: {cadenaInvertida}")

#3)
# Detector de números pares e impares: Escribe un programa que pida al usuario un número entero. Determina si el número es par o impar e imprime el resultado

num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print(f"el numero {num} es par.")
else:
    print(f"el numero {num} es impar.")

#4)
#Contador de vocales: Crea un programa que solicite al usuario una cadena de texto y cuente la cantidad de vocales presentes en la cadena. Imprime el resultado.


#ini = True
 
#while ini:
    texto = input("Escribe algo: ")
    a = texto.count("a")
    e = texto.count("e")
    i = texto.count("i")
    o = texto.count("o")
    u = texto.count("u")
    resultado = a+e+i+o+u
    print(f"Tu enunciado tiene {resultado} vocales")
    
    pregunta = input("Otra ves? ")
    pregunta = ''.join(pregunta.split())
 #   if pregunta.lower().startswith('s'):
  #      ini = True
   # else:
    #    ini = False

#5)
#Validador de contraseña: Escribe un programa que pida al usuario una contraseña. Lacontraseña debe tener al menos 8 caracteres, al menos una letra mayúscula, al menos unaletra minúscula y al menos un número. Imprime un mensaje indicando si la contraseñacumple con estos requisitos.

usuario = input("Ingresa una contraseña: ")
def verificar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False

    mayuscula = False
    minuscula = False
    numero = False

    for ingreso in contrasena:
        if ingreso.isupper():
            mayuscula = True
        elif ingreso.islower():
            minuscula = True
        elif ingreso.isdigit():
            numero = True
    return mayuscula and minuscula and numero


if verificar_contrasena(usuario):
    print("La contraseña cumple con los requisitos.")
else:
    print("La contraseña NO cumple con los requisitos.")