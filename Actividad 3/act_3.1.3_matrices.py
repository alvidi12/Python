"""
1. Crear un Arreglo [3][4] para luego ingresar elementos numéricos por pantalla utilizando doble for, mostrar los elementos por pantalla de forma ordenada como una matriz, tal cual muestra el ejemplo:

	 3	10	 4	16
	 1	 7 	 8	-7
	 9	-1	 3	 9

"""
matriz_2d_arreglo =[
    [3,10,4,16],
    [1,7,8,-7],
    [9,-1,3,9]
]
for i in matriz_2d_arreglo:
    for l in i:
        print(i)

"""
2. Crear un Arreglo [3][3][3] manualmente, los valores del arreglo pueden ser “amarillo”, “rojo”, “Naranja”, “Verde” y “Blanco”.
Una vez completado, mostrar la siguiente información:
●	Número de elementos “amarillo”.
●	Número de elementos “rojo”.
●	Número de elementos “Naranja”.
●	Número de elementos “Verde”.
●	Número de elementos “Blanco”

"""
lista = 0
matriz_3d_arreglo =[
    [
        [lista, "amarillo"]
    ],
    [
        [lista, "rojo"]
    ],
    [
        [lista, "naranjo"]
    ],
    [
        [lista, "verde"]
    ],
    [
        [lista, "blanco"]
    ]
]

resultado_m3_1 = matriz_3d_arreglo[0][0][0]
print(resultado_m3_1)
for i in matriz_3d_arreglo:
    for l in i:
        for j in i:
            print(j)

