import requests

ciudad = "Nueva York" #Cambiar la ciudad segun gusto.
api_key = "a2b3b130836df2b29363946fccb90e93"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&apiid={api_key}"

respuesta = requests.get(url).json()

if "main" in respuesta:
    clima = respuesta["weather"][0]["description"]
    temperatura = respuesta["main"]["temp"]
    humedad = respuesta["main"]["humidity"]
    presion = respuesta["main"]["pressure"]
    viento = respuesta["wind"]["speed"]

    print(f"Clima actual en {ciudad}")
    print(f"-Descripción del clima: {clima}")
    print(f"-Descripción Temperatura: {temperatura}")
    print(f"-Descripción Humedad: {humedad}")
    print(f"-Descripción Viento: {viento}")

else:
     print("error al obtener los datos del clima")