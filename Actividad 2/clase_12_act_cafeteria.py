#Ingreso de ventas diaras de los productos. Se debe generar informe de ventas.
#Solicitar ingreso de cantidad vendida de cada producto durante un día y calcular el total de ventas por producto y total de ventas diaras.
#Se debe imprimir un informe de ventas en la consola y guardarlo en un arhchivo de texto llamado "informe_ventas.txt"
"""
Requisitos:
1. Utilizar un ciclo repetitivo (for o while) para solicitar las ventas de cada producto.
2. Utilizar un if para verificar si se ingresó una cantidad válida.
3. Utiliza una función con try-except-finally para manejar errores y guardar el informe en un archivo de texto.
4. Manejar al menos dos tipos de errores: ValueError y otro más.
5. Investigar en internet como crear un archivo con python y el manejo de errores con Try-Except-Finally.
"""
while True:
    try:
        print("""*****Productos seleccionados:*****\n1) Pan Ciabatta: $2.000\n2) Pie de Limón: $3.500\n3) Café: $1.600\n4) Té: $1.600\n5) Alfajor: $1.000\n\n""")
        pan_ciabatta = float(input("Ingrese cantidad vendida de pan ciabatta: "))          
        pie_De_limon = float(input("Ingrese cantidad vendida de pie de limón: "))
        cafe = float(input("Ingrese cantidad vendida de café: "))
        te = float(input("Ingrese cantidad vendida de té: "))
        alfajor = float(input("Ingrese cantidad vendida de alfajor: "))
        while True:
            intento = input("\n¿Desea cambiar alguna información?")
            intentoMay = intento.lower()
            if intentoMay =="si":
                cambio = int(input("Ingrese el producto a cambiar: "))
                if cambio == 1: pan_ciabatta = float(input("Ingrese cantidad vendida de pan ciabatta: "))
                elif cambio == 2: pie_De_limon = float(input("Ingrese cantidad vendida de pie de limón: "))
                elif cambio == 3: cafe = float(input("Ingrese cantidad vendida de café: "))           
                elif cambio == 4: te = float(input("Ingrese cantidad vendida de alfajor: "))        
                elif cambio == 5: alfajor = float(input("Ingrese cantidad vendida de alfajor: "))  
            else: break

    except ValueError: print("Valor no válido.")
    intento = input("\n¿Reintentar nuevamente la operación?")
    intentoMay = intento.lower()
    if intentoMay == "no":
            break    
pan = pan_ciabatta*2000
pie = pie_De_limon*3500
cafe2= cafe*1600
te2= te*1600
alfajor2= alfajor*1000

print(f"""\nValor de productos vendidos del día:\n\nPan ciabatta ({pan_ciabatta:.0f} vendidos): {pan:.0f}\nPie de limón ({pie_De_limon:.0f} vendidos): {pie:.0f}\nCafé ({cafe:.0f} vendidos): {cafe2:.0f}\nTé ({te:.0f} vendidos): {te2:.0f}\nAlfajor ({alfajor:.0f} vendidos): {alfajor2:.0f}
      """)

ruta_archivo = "cafeteria.txt"
with open(ruta_archivo, "w")as archivo:
    archivo.write(f"""\nValor de productos vendidos del dia:\n\nPan ciabatta ({pan_ciabatta:.0f} vendidos): {pan:.0f}\nPie de limon ({pie_De_limon:.0f} vendidos): {pie:.0f}\nCafe ({cafe:.0f} vendidos): {cafe2:.0f}\nTe ({te:.0f} vendidos): {te2:.0f}\nAlfajor ({alfajor:.0f} vendidos): {alfajor2:.0f}
      """)