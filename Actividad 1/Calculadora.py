"""
2.Calculadora con funciones básicas + , - , * , / utilizando las funciones de Python def. 
"""
#Calculadora
num1 = int(input("Ingrese primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
operacion = input("Escriba la operación que desea aplicar: suma, resta, multiplicar, o dividir: ")

if operacion == "suma":
    resultado = num1+num2
if operacion == 'resta':
    resultado = num1-num2
if operacion == 'multiplicar':
    resultado = num1*num2
if operacion == 'dividir':
    resultado = num1/num2

    print("\nEl resultado es: ", resultado)

