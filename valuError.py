try:
    numero = int("abc") #Causara error porque se le esta asiganando una salida con letras a la función Int (solo numeros enteros)
except:
    print("Error de valor valueError")
else: print("si no hay error aparece el else")
finally: print("Esto se ejecuta si o si")
