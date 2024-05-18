
print("\nSe solicita ingreso de datos del empleador.\n")
usuario = input("Ingrese su nombre: ")
antiguedad = int(input("Ingrese el número de años de antigüedad en la empresa: "))
desempeño = input("Ingrese 'a', 'b', o 'c' según su desempeño en la empresa: ")
sueldo_base = 1000000

if antiguedad < 2 and desempeño =="a":
    sueldo = 0.05
elif antiguedad < 2 and desempeño == "b":
    sueldo = 0.03
elif antiguedad < 2 and desempeño == "c":
    sueldo = 0

elif 2 <= antiguedad <= 5 and desempeño =="a":
    sueldo = 0.08
elif 2 <= antiguedad <= 5 and desempeño == "b":
    sueldo = 0.05
elif 2 <= antiguedad <= 5 and desempeño == "c":
    sueldo = 0.02

elif antiguedad > 5 and desempeño == "a":
    sueldo = 0.12
elif antiguedad > 5 and desempeño == "b":
    sueldo = 0.08
elif antiguedad > 5 and desempeño == "c":
    sueldo = 0.05

print(f"Su bonificación es de ${sueldo_base*sueldo:.0f}\nSu sueldo total es de ${sueldo_base+sueldo:.0f}")

