#División por 0

try: resultado = 10/0
except ZeroDivisionError: print("No se puede dividir por 0")
finally: print("Esto se ejecuta si o si")