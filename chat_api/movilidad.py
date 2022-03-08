import time
import pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

# url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

# with open('C:/Users/steph/Documents/whatsapp-bot/data/Video-.txt') as f:
# text = f.readlines()

df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contacto_de_prueba.csv")
# df = pandas.read_csv("C:/Users/steph/Documents/whatsapp-bot/data/contactos-movilidad - contactos-movilidad.csv")

for index, contact in df.iterrows():
    nombre = contact['nombre']
    phone = contact['movil']
    message_body = {
        "phone": phone,
        "body": f'Hola {nombre}, '
                f'\n\n'
                f'Soy Jorge Torres del equipo de Antanas Mockus al Congreso de la República 🌻💚. '
                f'\n\n'
                f'Desde el Concejo de Bogotá impulsé la construcción de infraestructura en Bogotá: 130 km de '
                f'ciclorrutas 🚲, puentes de la Calle 63 y 127 con Avenida Boyacá 🚙, mejoramiento de estaciones y '
                f'nuevas troncales de Transmilenio, nuevos buses Euro VI y eléctricos🚍, y el acompañamiento y apoyo '
                f'técnico al Metro de Bogotá 🚆.. '
                f'\n\n'
                f'Ayúdanos con tu voto a llegar este 13 de marzo al Congreso de la República para seguir construyendo '
                f'sobre lo construido y mejorar la infraestructura de Bogotá. 🗳️ '
                f'\n\n'
                f'Ver video nuestra gestión y resultados 👇🏼'
                f'\n\n'
                f'https://www.youtube.com/watch?v=pqwXq--6pT8&ab_channel=JorgeTorres'
                f'\n\n'
                f'PD: Si quieres seguir en contacto, te agradezco respondas *TEMA*, para enviarte nuestra propuesta '
                f'en el tema de tu interés '
                f'\n\n'
                f'Si por el contrario no deseas seguir recibiendo mensajes envía la palabra *BAJA*. '}

    x1 = requests.post(url1, json=message_body)
    print(x1.text)
    time.sleep(30)
