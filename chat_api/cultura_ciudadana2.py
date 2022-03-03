import time
import pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

with open('C:/Users/steph/Documents/whatsapp-bot/data/super_civico.txt') as f:
    text = f.readlines()

# df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contactos_prueba.csv")
# df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contacto_de_prueba.csv")
df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contactos-cultura.csv")

link = f'{"https://chat.whatsapp.com/Bhh2AzCVhfYHy6XIyGCuwy"}'

for index, contact in df.iterrows():
    nombre = contact['nombre']
    phone = contact['movil']

    message_body = {
        "phone": phone,
        "body": f'Hola {nombre}, soy Jorge Torres del *Equipo de Mockus* al *Congreso de la República* 🥕. '
                f'En estos días nos encontramos en la calle '
                f'y nos comentaste que quieres que se recupere la *Cultura Ciudadana* en *Bogotá*. '
                f'Hemos realizado el siguiente video pedagógico para presentarte nuestra propuesta '
                f'para el Congreso. \n \n'
                f'Te invitamos a ver el *video* y a respaldarme '
                f'votando a la *Cámara por Bogotá* con el *número 110* del *Partido Alianza Verde*🌻.'
                f'\n\n'
                f'*#Verde110* 🌻🥕'
                f'\n\n'
                f'PD: Si quieres seguir en contacto, te agradezco me agregues dentro de tus contactos. '
                f'Si por el contrario no deseas seguir recibiendo mensajes envía la palabra *BAJA*. '}

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
