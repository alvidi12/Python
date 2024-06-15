import tkinter as tk # Importa el moóulo tkinter para la interfaz grafica
import requests # Importa un moóulo para hacer las solicitudes http a la API
import random
from io import BytesIO # Importa IO para los datos binarios
from PIL import Image, ImageTk # Para trabajar con las imágenes de los poke

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url) # Solicitud get a la API mediante la url
    
    if response.status_code == 200: #200 verifica si la solicitud fue exitosa
        data = response.json() # Convierte la respuesta en un formato json()
        nombre = data["name"] #Obtenemos el nombre del poke
        numero = data["id"] #Número del poke
        tipos = [tipos["type"]["name"] for tipos in data["types"]] #Obteniendo el tipo de poke

        resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipo: {', '.join(tipos)}" #Creando una cadena con saltos de líneas para obtener los datos del poke
        
        imagen_url = data["sprites"]["front_default"] #Obtener la img url con los datos de la API
        
        response_imagen = requests.get(imagen_url) #Realiza una solicitud get a la url
        imagen = Image.open(BytesIO(response_imagen.content)) #Abre la img con BytesIO
        imagen = imagen.resize((400,400), Image.Resampling.LANCZOS) #Redimensiona
        foto = ImageTk.PhotoImage(imagen) #Convierte la img a un objeto
        label_imagen.config(image=foto)
        label_imagen.image = foto #Guarda la referencia de la imagen
    else:
        resultado = "No se encontró el pokémon, debes atraparlo"
        label_imagen.config(image=None) #Elimina la img si no encuentra el poke
    
    label_resultado.config(text=resultado) #Configura la etiqueta label para mostrar la info del poke

def obtener_lista_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon["name"] for pokemon in data["results"]]
    else:
        return []

def buscar_pokemon_aleatorio():
    pokemon_aleatorio = obtener_lista_pokemon()
    pokemon_aleatorio = random.choice(pokemon_aleatorio)
    entry_pokemon.delete(0, tk.END) # Limpia la entrada actual
    entry_pokemon.insert(0, pokemon_aleatorio) # Inserta el nombre aleatorio
    buscar_pokemon()

windows = tk.Tk() #Creamos la ventana principal de la aplicación
windows.title("Busca tu Pokémon")

label_pokemon = tk.Label(windows, text="Ingresa el nombre del pokémon")
label_pokemon.pack() #Empaqueta el campo (en la ventana)

entry_pokemon = tk.Entry(windows) #Crea una entrada para recibir el nombre del poke
entry_pokemon.pack() #Empaqueta el campo (en la ventana)

button_buscar = tk.Button(windows, text="Buscar", command=buscar_pokemon)
button_buscar.pack() #Empaqueta el botón en la ventana

button_aleatorio = tk.Button(windows, text="Poke Aleatorio", command=buscar_pokemon_aleatorio)
button_aleatorio.pack()

label_resultado = tk.Label(windows, text="") #Creamos una etiqueta vacía para mostrar los resultados de la búsqueda
label_resultado.pack() #Empaqueta el campo (en la ventana)

label_imagen = tk.Label(windows) #Una etiqueta para mostrar el poke
label_imagen.pack()

windows.mainloop() #Inicia el bucle principal para que se ejecute la aplicación