def nombre_usuario():
    while True:
        nombre = input("Ingrese usuario: ")
        if len(nombre) == 0:
            print("No ha puesto ningún usuario.")
        elif len(nombre) > 30:
            print("Excedió el límite de caracteres (30).\nVuelva a intentarlo.")
        else:
            break

# Llama a la función para validar el nombre de usuario
nombre_usuario()

def cantidad_peso():
    while True:
        try:
            peso = float(input("Ingrese peso del paquete (Kg): "))
            return peso  # Devuelve el valor ingresado
        except ValueError:
            print("Error de ingreso. Intente nuevamente.")

# Llama a la función para validar el peso
pesototal = cantidad_peso()

def cantidad_kilometro():
    while True:
        try:
            distancia = float(input("Ingrese distancia de envío (Km): "))
            return distancia  # Devuelve el valor ingresado
        except ValueError:
            print("Error de ingreso. Intente nuevamente.")

# Llama a la función para validar la distancia
kilometrototal = cantidad_kilometro()

# Cálculo del costo del envío
costoBase = 5000
exceso_Kg = 500
exceso_Km = 100

if pesototal > 30:
    PF_kg = (pesototal - 30) * exceso_Kg + costoBase
else:
    PF_kg = 0

if kilometrototal > 100:
    PF_km = (kilometrototal - 100) * exceso_Km + costoBase
else:
    PF_km = 0

CostoTotal = PF_kg + PF_km + costoBase

# Mostrar costo de envío
print(f"El costo total del envío es: ${CostoTotal:.0f}")
