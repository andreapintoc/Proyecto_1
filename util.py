import json
import requests

def leer_data(): #abrir el json de datos de usuarios
    with open('data.json', 'r') as data:
        return json.load(data) 
     
def escribir_data(datos): #Escrbir en el json los datos registrdos
    with open('data.json', 'w') as data:
        json.dump(datos, data, indent=4)

def obtener_inventario(): #obtener los datos del api
    url = "https://api-escapamet.vercel.app/"
    respuesta = requests.get(url)
    return json.loads(respuesta.text)