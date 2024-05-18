import requests

ciudad = "Port Montt"  # Cambia la ciudad a tu gusto
api_key = "4d910fffa7f7174c116caf7f31266b37"  # Reemplaza con tu clave de API
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

respuesta = requests.get(url).json()

if "main" in respuesta:
    clima = respuesta["weather"][0]["description"]
    temperatura = respuesta["main"]["temp"]
    humedad = respuesta["main"]["humidity"]
    presion = respuesta["main"]["pressure"]
    viento = respuesta["wind"]["speed"]

    print(f"Clima actual en {ciudad}")
    print(f"-Descripción del clima: {clima}")
    print(f"-Descripción Temperatura: {int(temperatura-273.15)}")
    print(f"-Descripción Humedad: {humedad}")
    print(f"-Descripción Viento: {viento}")
else:
    print("Error al obtener datos del clima.")