import pandas
import requests

url1 = 'https://api.chat-api.com/instance409704/sendMessage?token=krz6j7h0urdw4qj1'

url2 = 'https://api.chat-api.com/instance409704/sendFile?token=krz6j7h0urdw4qj1'

with open('E:\\whatsapp-bot\\data\\salud_mp4.txt') as f:
    text = f.readlines()

#df = pandas.read_csv("E:\\whatsapp-bot\\data\\contactos_prueba.csv")
df = pandas.read_csv("E:\\whatsapp-bot\\data\\contacto_de_prueba.csv")

for index, contact in df.iterrows():
    print('Enviando mensaje')
    nombre = contact['nombre']
    phone = contact['movil']

    message_body = {
        "phone": phone,
        "body": f'Hola {nombre}. Soy Jorge Torres 🌻. '
                f'La salud ha sido un gran dolor de cabeza para los colombianos. '
                f' La corrupción y la ineficiencia afectaron todo el sistema de salud.'
                f' Cuando fui concejal de Bogotá trabajé arduamente por mejorar la calidad de la salud.'
                f' Con tu apoyo quiero llegar al Congreso de la República para ser aliados del personal '
                f'de la salud y trabajar por la dignidad de los colombianos.'
                'El *13 de marzo* activa tu poder ciudadano y *VOTA* '
                '✏️ marcando Partido Alianza Verde 🌻 Número 110 de la Cámara de Representantes por Bogotá. 🥕'
                'Gracias 💚 #Verde110' 
                f' \n\nSi quieres seguir en contacto, te agradezco me agregues dentro de tus contactos.'
                f' Para no seguir recibiendo mensajes envía *BAJA*'}

    photo_body = {
        "phone": 61451961237,
        "body": text[0],
        "filename": "salud.mp4",
        "caption": "El *13 de marzo* activa tu poder ciudadano y VOTA. Gracias 💚 #Verde110"
    }

    x1 = requests.post(url1, json=message_body)
    x2 = requests.post(url2, json=photo_body)
    print(x1.text)
    print(x2.text)