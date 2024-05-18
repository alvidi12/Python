#ETAPA 1:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

Edad = int(input("Ingrese su edad: "))
if Edad <18: print("Usted es MENOR de edad.")
else: print("Usted es MAYOR de edad")

#ETAPA 2:
#Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
#User1: pedro   	Contraseña1: 1234
#User2: angel		Contraseña2: a4s1

user = input("ingrese su usuario: ")
pwd = input("Ingrese su contraseña: ")

if user == "pedro" and pwd == "1234":print ("Bienvenido")
elif user == "angel" and pwd == "a4si": print("Bienvenido")
else:print ("Error en contraseña")

#ETAPA 3:
#Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

Nota1= int(input("Ingrese primera nota: "))
Nota2= int(input("Ingrese primera nota: "))
Nota3= int(input("Ingrese primera nota: "))
Resultado = (Nota1+Nota2+Nota3)/3

if Resultado >= 4.0:
    print(f"APROBADO, su promedio fue de {Resultado:.1f}")
else: print(f"REPROBADO, su promedio fue de {Resultado:.1f}")

#ETAPA 4:
#Crear una salida por pantalla con la siguiente información:
#¿Cuál de los siguientes animales vive en el agua?
#Perro
#Cocodrilo
#Conejo
#Tiburón
#Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la res-puesta es Tiburón asignar +1.0 a puntaje, del cualquier otro caso, no asignar valor, finalmente crear una salida por panta-lla para mostrar el puntaje obtenido.

Animal = input("""
Perro
Cococdrillo
Conejo
Tiburón

¿Cuál de los siguientes animales vive en el agua?: """)

if Animal == "Cocodrillo": print("+0.5 Puntos!")
elif Animal == "Tiburón": print("+1.0 Puntos!")
else: print("0 puntos")

#ETAPA 5:
#De la misma forma del ejercicio anterior, debes crear un formulario con 3 pre-guntas (4 respuestas por cada pregunta) de un tema a elección, ya sea pe-lículas, series, caricaturas, entre otras.
#Asignar puntaje a cada pregunta y dependiendo del puntaje generar una escala de notas, así cuando los usuarios respondan las 3 preguntas se les muestra mediante una salida por pantalla su puntaje obtenido y la nota que equivale.

print("Bienvenido al tema de 'Cotidiano' ,aquí veremos si tienes algo de talento:\n")
pregunta1 = input("""#1. De estos 4 deportes, ¿A cuál se le acomodaría mejor a Diego Maradona?

baloncesto
golf
tenis
ufc
                  
Respuesta: """)
pregunta2 = input("""\n#2. ¿Cuál de estas 4 opciones de dejaría con mas amsiedad?

caminar
dormir
trotar
correr
                  
Respuesta: """)
pregunta3 = input("""\n#3. ¿Cuál de estos 4 tipos de placa de desarrollo te podría servir como llavero?

raspberry pi
arduino
nvidia jetson nano
pic
                  
Respuesta: """)

if pregunta1 == "golf":
    pregunta1 = 5
elif pregunta1 == "tenis":
    pregunta1 = 4
elif pregunta1 == "baloncesto":
    pregunta1 = 2
else:
    pregunta1 = 0

if pregunta2 == "dormir":
    pregunta2 = 5
elif pregunta2 == "caminar":
     pregunta2 = 4
elif pregunta2 == "trotar":
    pregunta2 = 2
else:
    pregunta2 = 0

if pregunta3 == "pic":
    pregunta3 = 5
elif pregunta3 == "arduino":
    pregunta3 = 4
elif pregunta3 == "raspberry pi":
    pregunta3 = 3
else:
    pregunta3 = 0

puntos = pregunta1+pregunta2+pregunta3
if puntos == 15: print(f"\nSu puntuación fue de {puntos} de 15, eres aceptable.")
elif puntos >= 7: print(f"\nSu puntuación fue de {puntos} de 15, no te falta talento pero ni te sobra.")
else:
    print(f"\nSu puntuación fue de {puntos} de 15, no tienes talento.")