import time
import pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

with open('/data/poder_ciudadano.txt') as f:
    text = f.readlines()

df = pandas.read_csv("E:\\whatsapp-bot\\data\\contactos_prueba.csv")
#df = pandas.read_csv("E:\\whatsapp-bot\\data\\contacto_de_prueba.csv")

for index, contact in df.iterrows():
    nombre = contact['nombre']
    phone = contact['movil']
    message_body = {
        "phone": phone,
        "body": f'Hola {nombre}. Soy Jorge Torres 🌻. He sido un promotor de la cultura ciudadana y '
                f' la defensa de la vida. '
                f'Creo en la pedagogía como herramienta política para construir un mejor país. '
                f'Estoy convencido que la acción colectiva y la corresponsabilidad entre Estado '
                f'y ciudadanía son el camino para impulsar los cambios que requiere Colombia. '
                f'Quiero dar más para que todos podamos vivir mejor. Soy Mockusiano al 110%. '
                f'Te invito a respaldarme votando a la *Cámara por Bogotá 🌻 Verde110* 🥕'
                f'\n PD: Si quieres seguir en contacto, te agradezco me *agregues* dentro de tus contactos. '
                f'Para no seguir recibiendo mensajes envía *BAJA*'}

    photo_body = {
        "phone": phone,
        "body": text[0],
        "filename": "salud.mp4",
        "caption": "El *13 de marzo* activa tu poder ciudadano y VOTA. Gracias 💚 #Verde110"
    }

    x1 = requests.post(url1, json=message_body)
    x2 = requests.post(url2, json=photo_body)
    print(x1.text)
    print(x2.text)
    time.sleep(10)
