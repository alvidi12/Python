print("\n*********************************\nCálculo de liquidación de sueldo:\n*********************************\n")

# 1) Ingreso de datos del trabajor.

while True: #Ingreso para el nombre del trabajador.
        nombre = input("Ingrese nombre del trabajor: ")
        if len(nombre) == 0: print("No debe quedar espacio en blanco.") 
        elif len(nombre) > 30: print("excedió el límite de caracteres (30)\nVuelva a intentarlo. ")
        else: break

def sueldo_base():  #Ingreso del sueldo base del trabajador.
    while True:
        try:
            sueldo = float(input("Ingrese el sueldo base del trabajador: "))
            if sueldo < 0: print("No debe ingresar números negativos.")
            else: return sueldo
        except ValueError: print("Error de ingreso.")
sueldo = sueldo_base()

def horas_extras(): #Ingreso de las horas trabajadas de forma mensual
    while True:
        try:
            Hr_Extras = float(input("Ingrese las horas trabajadas en el mes: "))
            if Hr_Extras < 0: print("No debe ingresar números negativos.")
            else: return Hr_Extras
            return Hr_Extras
        except ValueError: print("Error de ingreso.")
Hr_Extras = horas_extras()

# 2) Cálculo de la liquidación.

if Hr_Extras > 180: muestra_hr = Hr_Extras-180  #Muestra de dias extras trabajados
else: muestra_hr = 0

dia_pago = sueldo/180   #Calculo de pago dia normal trabajado segun sueldo base
pago_extra = muestra_hr*dia_pago #Caclulo de pago de solo horas extras
if Hr_Extras > 180: extra = pago_extra*1.5 #Calculo de horas extras a pagar
else: extra = 0

ingreso_total = sueldo + extra
fonasa = ingreso_total*0.07
afp = ingreso_total*0.10
sueldo_neto = ingreso_total - fonasa -afp
desc_seguridad_s = fonasa+afp
# 3) Mostrar la liquidación.

print(f"\nEstimado {nombre}, aquí tiene un desglose de su liquidación ingresada:\nSueldo base: ${sueldo:.0f}\nHoras extras trabajadas: {muestra_hr:.0f}\nPago adicional de horas extras: ${extra:.0f}\nTotal de ingresos: ${ingreso_total:.0f}\nDescuento de seguridad social: ${desc_seguridad_s:.0f}\nSueldo neto (Final): ${sueldo_neto:.0f}")

# 4) Generar archivo de liquidación.

import os
archivo = f"liquidacion_{nombre}.docx"

with open(archivo, "w")as ruta:
    ruta.write(f"\nEstimado {nombre}: Aqui tiene un desglose de su liquidacion ingresada:\n\nSueldo base: ${sueldo:.0f}\nHoras extras trabajadas: {muestra_hr:.0f}\nPago adicional de horas extras: ${extra:.0f}\nTotal de ingresos: ${ingreso_total:.0f}\nDescuento de seguridad social: ${desc_seguridad_s:.0f}\nSueldo neto (Final): ${sueldo_neto:.0f}")
    print("\n\nSe ha creado un archivo Word(.docx) con los datos entregados de liquidación.\n")