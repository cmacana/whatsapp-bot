import time
import pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

with open('E:\\whatsapp-bot\\data\\super_civico.txt') as f:
    text = f.readlines()

df = pandas.read_csv("E:\\whatsapp-bot\\data\\contactos_prueba.csv")
#df = pandas.read_csv("E:\\whatsapp-bot\\data\\contacto_de_prueba.csv")

for index, contact in df.iterrows():
    nombre = contact['nombre']
    phone = contact['movil']
    message_body = {
        "phone": phone,
        "body": f'Hola {nombre}. Soy Jorge Torres del equipo de *💚🌻 Mockus al Congreso 🌻💚*. '
                f'Hace unos dias nos encontramos en la calle '
                f'y nos comentaste que querias recuperar la *🌻cultura ciudadana🥕* en Bogotá. '
                f'Hemos preparado el siguiente video para presentarte nuestra propuesta para recuperar '
                f'la cultura ciudadana con acciones desde el Congreso de la República . \n \n'
                f'Te invitamos a ver el *video* y a respaldarme '
                f'votando a la *Cámara por Bogotá 🌻 Verde110* 🥕.'
                f'\n\n'
                f'PD: Si quieres seguir en contacto, te agradezco me *agregues* dentro de tus contactos '
                f'y repondas con la palabra *CONTACTO*. '
                f'Si por el contrario no deseas  seguir recibiendo mensajes envía la palabra *BAJA*'}

    photo_body = {
        "phone": phone,
        "body": text[0],
        "filename": "super_civico.mp4",
        "caption": "Por la recuperación de la cultura ciudadana en Bogotá, este *13 de marzo* activa tu "
                   "poder ciudadano y *VOTA*: 💚 #Verde110"
    }

    x1 = requests.post(url1, json=message_body)
    x2 = requests.post(url2, json=photo_body)
    print(x1.text)
    print(x2.text)
    time.sleep(10)
