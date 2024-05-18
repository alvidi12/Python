# ACT 1
# Analiza el siguiente código que debe aplicar descuentos por rangos de edad.

edad = int(input ("Ingrese su edad "))
if edad > 0 and edad < 18: print (f"Edad: {edad} ,tiene descuento de un 50% ")
elif edad >= 18 and edad < 30: print (f"Edad: {edad} ,tiene descuento de un 20%")
elif edad > 60: print (f"Edad: {edad} ,tiene descuento de un 90%")
else: print (f"Edad: {edad} ,no aplica descuento")

# ACT 2
#  Observa el siguiente código, falta una sentencia

# validación user y pass
user = input("ingrese su user")
pwd = input("Ingrese su pass")

if user == "andy" and pwd == "andy":print ("Bienvenido")
else:print ("Error en contraseña")

# ACT 3 
#Devolución Dinero
user = input("Ingrese el usuario: ")
pwd = input("Ingrese su password: ")
if user == "duoc" and pwd == "123duoc":
    valorDev = int(input("Bienvenido, Ingrese el valor a devolver: "))
    if valorDev > 100000: print("Se dará la máxima urgencia a su devolución de dinero")
    else: print("El caso ha quedado registrado, le informaremos lo antes posible") 
else: print ("Error en contraseña")