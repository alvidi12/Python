#calcular el costo de envío de paquetes para una empresa de logística

print("\n***************************************\nCálculo de costo de envío de paquetes.\nDistancia estandar: 100 Km.\nPeso estandar: 30 kg\nPrecio: $ 5.000\n***************************************\n")

#Ingreso de datos del paquete
def nombre_usuario():
    while True:
        nombre = input("Ingrese usuario: ")
        if len(nombre) == 0: print("No ha puesto ningun usuario.") 
        elif len(nombre) > 30: print("excedió el límite de caracteres (30)\nVuelva a intentarlo. ")
        else: break
nombre_usuario()

def cantidad_peso():
    while True:
        try:
            peso = float(input("Ingrese peso del paquete (Kg): "))
            return peso
        except ValueError: print("Error de ingreso.")
pesototal = cantidad_peso()

def cantidad_kilometro():
    while True:
        try:
            distancia = float(input("Ingrese distancia de envío (Km): "))
            return distancia
        except ValueError: print("Error de ingreso.")
kilometrototal = cantidad_kilometro()

#Cálculo del costo del envío
costoBase = 5000
exceso_Kg = 500
exceso_Km = 100

if pesototal > 30: PF_kg = (pesototal - 30)*exceso_Kg + costoBase
else: PF_kg = 0

if kilometrototal > 100: PF_km = (kilometrototal - 100)*exceso_Km + costoBase
else: PF_km = 0
CostoTotal = PF_kg + PF_km + costoBase

#Mostrar costo de envío
print(f"${CostoTotal:.0f}")

"""
○ Mostrar un desglose del costo de envío, incluyendo el nombre del cliente, el
peso del paquete, la distancia de envío, el costo base, el adicional por peso,
el recargo por distancia (si corresponde) y el costo total de envío, todo
ordenado y bien presentado.
"""

#Generar archivo de envío
"""
 Crear un archivo de texto (.txt) con los datos del envío.
○ El archivo generado debe incluir el nombre del cliente, el peso del paquete, la
distancia de envío y el costo total de envío, todo de forma ordenada y bien
presentada.
○ El nombre del archivo generado debe seguir el formato
"envio_[nombre_cliente].txt".
"""
