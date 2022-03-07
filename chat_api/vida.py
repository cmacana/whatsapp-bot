import time
import pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

with open('C:/Users/steph/Documents/whatsapp-bot/data/Video-Vida.txt') as f:
    text = f.readlines()

# df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contacto_de_prueba.csv")
df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contactos-vida.csv")

tema = 'salud'
for index, contact in df.iterrows():
    nombre = contact['nombre']
    phone = contact['movil']
    message_body = {
        "phone": phone,
        "body": f'Hola {nombre}, '
                f'\n\n'
                f'Hace unos dias nos encontramos en la calle '
                f'y nos comentaste que te interesaba mejorar la *protección de la vida y la seguridad*'
                f'🌻🏥 en Bogotá. '
                f'\n\n'
                f'El profe *Antanas Mockus* nos enseñó que “cuando uno aprende a respetar la vida, '
                f'aprende a respetar los otros derechos”. '
                f'\n\n'
                f'Por eso quiero llegar al Congreso para mejorar *la convivencia y la seguridad* en la ciudad, '
                f'y así cuidar la vida en todas sus formas, sin ejercer violencia en contra ningún ser vivo. '
                f'*Construyamos juntos este proyecto y ayúdame con tu voto, el de tu familia y tus amigos votando este '
                f'13 de marzo a la Cámara por Bogotá* 🌻*Verde 110*🥕 '
                f'\n'
                f'PD: Si quieres seguir en contacto, te agradezco respondas *TEMA*, para enviarte nuestra propuesta '
                f'en el tema de tu interés '
                f'\n\n'
                f'Si por el contrario no deseas seguir recibiendo mensajes envía la palabra *BAJA*. '}

    photo_body = {
        "phone": phone,
        "body": text[0],
        "filename": "salud.mp4",
        "caption": "Por *la vida y la seguridad*, este *13 de marzo* activa tu "
                   "poder ciudadano y *VOTA*: 💚 #Verde110"
    }

    x1 = requests.post(url1, json=message_body)
    x2 = requests.post(url2, json=photo_body)
    print(x1.text)
    print(x2.text)
    time.sleep(30)
